#!/usr/bin/env python3
"""Validate curriculum structure, links, research config, and publication safety."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "CURRICULUM.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "docs/curriculum/README.md",
    "docs/curriculum/competency-framework.md",
    "docs/curriculum/catalog.json",
    "docs/curriculum/learning-contract.md",
    "docs/curriculum/assessment.md",
    "docs/curriculum/fde-capstone.md",
    "docs/curriculum/course-unit-template.md",
    "docs/governance/course-governance.md",
    "docs/governance/source-selection-standard.md",
    "docs/governance/research-to-course.md",
    "docs/governance/publication-safety.md",
    "research/README.md",
    "research/reading-list.md",
    "research/paper-note-template.md",
    "research/sources.json",
    "research/radar/latest.md",
]
ABILITY_IDS = {"BIZ", "HAI", "ENG", "EVAL", "DOMAIN", "CS", "AGENT", "FDE"}
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PUBLISHABLE_SUFFIXES = {".md", ".html", ".css", ".json", ".yml", ".yaml", ".txt"}
SKIP_PARTS = {".git", "__pycache__", ".pytest_cache"}
PRIVACY_PATTERNS = [
    ("Windows absolute path", re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:\\")),
    ("macOS user profile path", re.compile(r"/Users/[A-Za-z0-9._-]+/")),
    ("Linux user profile path", re.compile(r"/home/[A-Za-z0-9._-]+/")),
]
SECRET_PATTERNS = [
    ("OpenAI-style API key", re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{16,}")),
    ("GitHub token", re.compile(r"gh[pousr]_[A-Za-z0-9]{16,}")),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z_-]{20,}")),
    (
        "private key",
        re.compile(r"BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY"),
    ),
]
EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@([A-Z0-9.-]+\.[A-Z]{2,})\b", re.IGNORECASE)
ALLOWED_EMAIL_DOMAINS = {
    "example.com",
    "users.noreply.github.com",
}


def iter_public_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() in PUBLISHABLE_SUFFIXES or path.suffix.lower() == ".py":
            yield path


def check_publication_safety() -> list[str]:
    errors: list[str] = []
    for path in iter_public_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT)

        if path.suffix.lower() in PUBLISHABLE_SUFFIXES:
            for label, pattern in PRIVACY_PATTERNS:
                if pattern.search(text):
                    errors.append(f"publication safety: {relative} contains {label}")
            for match in EMAIL_PATTERN.finditer(text):
                domain = match.group(1).lower()
                if domain not in ALLOWED_EMAIL_DOMAINS:
                    errors.append(
                        f"publication safety: {relative} contains a non-placeholder email"
                    )
                    break

        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"publication safety: {relative} contains possible {label}")
    return errors




def check_required() -> list[str]:
    return [f"missing required file: {path}" for path in REQUIRED if not (ROOT / path).is_file()]


def check_internal_links() -> list[str]:
    errors: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if (
                target.startswith(("http://", "https://", "mailto:", "#"))
                or re.match(r"^[A-Za-z]:[\\/]", target)
            ):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (markdown.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                errors.append(f"broken link: {markdown.relative_to(ROOT)} -> {raw_target}")
    return errors


def check_ability_model() -> list[str]:
    path = ROOT / "docs" / "curriculum" / "competency-framework.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    missing = sorted(ability for ability in ABILITY_IDS if f"| {ability} |" not in text)
    return [f"missing ability id in competency framework: {ability}" for ability in missing]


def check_research_sources() -> list[str]:
    path = ROOT / "research" / "sources.json"
    if not path.exists():
        return []
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid research source config: {exc}"]
    if not isinstance(data.get("max_total"), int) or data["max_total"] < 1:
        errors.append("research sources max_total must be a positive integer")
    queries = data.get("queries")
    if not isinstance(queries, list) or not queries:
        errors.append("research sources must contain queries")
        return errors
    for index, query in enumerate(queries):
        for field in ("name", "search_query", "max_results"):
            if field not in query:
                errors.append(f"research query {index} missing {field}")
    return errors


def check_curriculum_catalog() -> list[str]:
    path = ROOT / "docs" / "curriculum" / "catalog.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid curriculum catalog: {exc}"]

    modules = data.get("modules")
    if not isinstance(modules, list) or not modules:
        return ["curriculum catalog must contain modules"]

    errors: list[str] = []
    ids: list[str] = []
    for index, module in enumerate(modules):
        if not isinstance(module, dict):
            errors.append(f"catalog module {index} must be an object")
            continue
        for field in (
            "id", "title", "stage", "duration_weeks",
            "prerequisites", "page", "build"
        ):
            if field not in module:
                errors.append(f"catalog module {index} missing {field}")
        module_id = module.get("id")
        if isinstance(module_id, str):
            ids.append(module_id)
        if (
            not isinstance(module.get("duration_weeks"), int)
            or module.get("duration_weeks", 0) < 1
        ):
            errors.append(f"catalog module {module_id or index} has invalid duration")
        if not isinstance(module.get("build"), str) or not module.get("build", "").strip():
            errors.append(f"catalog module {module_id or index} must define a build")

    duplicate_ids = sorted({module_id for module_id in ids if ids.count(module_id) > 1})
    errors.extend(f"duplicate catalog module id: {module_id}" for module_id in duplicate_ids)
    known_ids = set(ids)
    graph: dict[str, list[str]] = {}
    readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")

    for module in modules:
        if not isinstance(module, dict) or not isinstance(module.get("id"), str):
            continue
        module_id = module["id"]
        prerequisites = module.get("prerequisites")
        if not isinstance(prerequisites, list):
            errors.append(f"catalog module {module_id} prerequisites must be a list")
            prerequisites = []
        graph[module_id] = [item for item in prerequisites if isinstance(item, str)]
        for prerequisite in graph[module_id]:
            if prerequisite not in known_ids:
                errors.append(
                    f"catalog module {module_id} has unknown prerequisite {prerequisite}"
                )
            if prerequisite == module_id:
                errors.append(f"catalog module {module_id} depends on itself")

        page = module.get("page")
        if isinstance(page, str):
            resolved = (path.parent / page).resolve()
            if not resolved.is_file():
                errors.append(f"catalog module {module_id} page does not exist: {page}")
            expected_link = f"(docs/curriculum/{page})"
            if expected_link not in readme:
                errors.append(f"README does not link catalog module {module_id}: {page}")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(module_id: str) -> None:
        if module_id in visiting:
            errors.append(f"curriculum prerequisite cycle includes {module_id}")
            return
        if module_id in visited:
            return
        visiting.add(module_id)
        for prerequisite in graph.get(module_id, []):
            if prerequisite in graph:
                visit(prerequisite)
        visiting.remove(module_id)
        visited.add(module_id)

    for module_id in graph:
        visit(module_id)

    core_weeks = sum(
        module.get("duration_weeks", 0)
        for module in modules
        if isinstance(module, dict) and module.get("stage") != "elective"
    )
    if data.get("core_estimated_weeks") != core_weeks:
        errors.append(
            f"catalog core_estimated_weeks is {data.get('core_estimated_weeks')}, "
            f"expected {core_weeks}"
        )
    return errors


def main() -> int:
    errors = (
        check_required()
        + check_internal_links()
        + check_ability_model()
        + check_research_sources()
        + check_curriculum_catalog()
        + check_publication_safety()
    )
    if errors:
        print("Curriculum validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Curriculum validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
