#!/usr/bin/env python3
"""Fetch recent arXiv papers and render a review queue for the curriculum."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCES = ROOT / "research" / "sources.json"
DEFAULT_OUTPUT = ROOT / "research" / "radar" / "latest.md"
ARXIV_API = "https://export.arxiv.org/api/query"
ATOM_NS = "http://www.w3.org/2005/Atom"
ARXIV_NS = "http://arxiv.org/schemas/atom"

KEYWORDS = {
    "agent": 2,
    "agentic": 2,
    "tool": 2,
    "planning": 2,
    "evaluation": 2,
    "benchmark": 2,
    "reliability": 3,
    "safety": 3,
    "security": 3,
    "long-horizon": 3,
    "software engineering": 2,
    "human-ai": 2,
    "enterprise": 2,
    "workflow": 1,
    "retrieval": 1,
}


@dataclass(frozen=True)
class Paper:
    title: str
    url: str
    published: str
    updated: str
    authors: tuple[str, ...]
    summary: str
    categories: tuple[str, ...]
    source: str


def clean_text(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def parse_atom(xml_text: str, source: str) -> list[Paper]:
    root = ET.fromstring(xml_text)
    papers: list[Paper] = []
    for entry in root.findall(f"{{{ATOM_NS}}}entry"):
        title = clean_text(entry.findtext(f"{{{ATOM_NS}}}title"))
        summary = clean_text(entry.findtext(f"{{{ATOM_NS}}}summary"))
        published = clean_text(entry.findtext(f"{{{ATOM_NS}}}published"))
        updated = clean_text(entry.findtext(f"{{{ATOM_NS}}}updated"))
        authors = tuple(
            clean_text(node.findtext(f"{{{ATOM_NS}}}name"))
            for node in entry.findall(f"{{{ATOM_NS}}}author")
        )
        categories = tuple(
            node.attrib.get("term", "")
            for node in entry.findall(f"{{{ATOM_NS}}}category")
            if node.attrib.get("term")
        )
        url = clean_text(entry.findtext(f"{{{ATOM_NS}}}id"))
        for link in entry.findall(f"{{{ATOM_NS}}}link"):
            if link.attrib.get("rel") == "alternate":
                url = link.attrib.get("href", url)
                break
        if title and url:
            papers.append(
                Paper(
                    title=title,
                    url=url,
                    published=published,
                    updated=updated,
                    authors=authors,
                    summary=summary,
                    categories=categories,
                    source=source,
                )
            )
    return papers


def relevance_score(paper: Paper) -> int:
    haystack = f"{paper.title} {paper.summary}".lower()
    return sum(weight for keyword, weight in KEYWORDS.items() if keyword in haystack)


def deduplicate(papers: Iterable[Paper]) -> list[Paper]:
    by_url: dict[str, Paper] = {}
    for paper in papers:
        key = re.sub(r"v\d+$", "", paper.url.rstrip("/"))
        current = by_url.get(key)
        if current is None or paper.updated > current.updated:
            by_url[key] = paper
    return list(by_url.values())


def fetch_query(query: dict, timeout: int = 30) -> list[Paper]:
    params = urllib.parse.urlencode(
        {
            "search_query": query["search_query"],
            "start": 0,
            "max_results": int(query.get("max_results", 10)),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    request = urllib.request.Request(
        f"{ARXIV_API}?{params}",
        headers={"User-Agent": "ai-business-delivery-curriculum/0.1"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read().decode("utf-8")
    return parse_atom(body, query["name"])


def compact_summary(summary: str, limit: int = 320) -> str:
    if len(summary) <= limit:
        return summary
    return summary[: limit - 1].rstrip() + "…"


def render_markdown(papers: list[Paper], generated_on: str) -> str:
    lines = [
        "# 最新研究候选",
        "",
        f"生成日期：{generated_on}。",
        "",
        "> 本页由脚本自动生成，只是待审队列，不代表课程推荐。论文必须经过人工初筛、深读和复现实验。",
        "",
    ]
    if not papers:
        lines.extend(["当前没有抓取到候选论文。", ""])
        return "\n".join(lines)

    grouped: dict[str, list[Paper]] = {}
    for paper in papers:
        grouped.setdefault(paper.source, []).append(paper)

    for source, group in grouped.items():
        lines.extend([f"## {source}", ""])
        for paper in group:
            author_text = ", ".join(paper.authors[:4])
            if len(paper.authors) > 4:
                author_text += " 等"
            published = paper.published[:10] or "日期未知"
            categories = ", ".join(paper.categories[:4]) or "未标注"
            lines.extend(
                [
                    f"### [{paper.title}]({paper.url})",
                    "",
                    f"- 日期：{published}",
                    f"- 作者：{author_text or '未知'}",
                    f"- 分类：{categories}",
                    f"- 相关性分：{relevance_score(paper)}",
                    f"- 摘要：{compact_summary(paper.summary)}",
                    "- 人工评审：待处理",
                    "",
                ]
            )
    return "\n".join(lines)


def load_sources(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data.get("queries"), list) or not data["queries"]:
        raise ValueError("research/sources.json must contain a non-empty queries list")
    return data


def collect_papers(config: dict) -> tuple[list[Paper], list[str]]:
    papers: list[Paper] = []
    warnings: list[str] = []
    for query in config["queries"]:
        try:
            papers.extend(fetch_query(query))
        except Exception as exc:  # Network failures should name the affected source.
            warnings.append(f"{query.get('name', 'unknown')}: {exc}")
    ranked = sorted(
        deduplicate(papers),
        key=lambda paper: (relevance_score(paper), paper.published),
        reverse=True,
    )
    return ranked[: int(config.get("max_total", 24))], warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args(argv)

    config = load_sources(args.sources)
    papers, warnings = collect_papers(config)
    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    if not papers:
        print("No papers fetched; existing radar was left unchanged.", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_markdown(papers, args.date), encoding="utf-8")
    print(f"Wrote {len(papers)} candidates to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
