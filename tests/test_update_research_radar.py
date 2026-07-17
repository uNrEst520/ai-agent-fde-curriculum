from __future__ import annotations

import importlib.util
import unittest
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "research_radar", ROOT / "scripts" / "update_research_radar.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class ResearchRadarTests(unittest.TestCase):
    def setUp(self):
        sample = ROOT / "tests" / "fixtures" / "arxiv_sample.xml"
        self.xml_text = sample.read_text(encoding="utf-8")

    def test_parse_atom_extracts_paper(self):
        papers = MODULE.parse_atom(self.xml_text, "test source")
        self.assertEqual(len(papers), 1)
        self.assertEqual(
            papers[0].title,
            "Reliable Tool-Use Agents for Long-Horizon Workflows",
        )
        self.assertEqual(papers[0].categories, ("cs.AI",))
        self.assertEqual(papers[0].source, "test source")

    def test_relevance_score_rewards_reliability_and_safety(self):
        paper = MODULE.parse_atom(self.xml_text, "test source")[0]
        self.assertGreaterEqual(MODULE.relevance_score(paper), 10)

    def test_deduplicate_ignores_arxiv_version_suffix(self):
        paper = MODULE.parse_atom(self.xml_text, "test source")[0]
        older = MODULE.Paper(
            title=paper.title,
            url=paper.url.replace("v2", "v1"),
            published=paper.published,
            updated="2026-01-02T00:00:00Z",
            authors=paper.authors,
            summary=paper.summary,
            categories=paper.categories,
            source=paper.source,
        )
        result = MODULE.deduplicate([older, paper])
        self.assertEqual(result, [paper])

    def test_render_marks_page_as_candidate_queue(self):
        paper = MODULE.parse_atom(self.xml_text, "test source")[0]
        rendered = MODULE.render_markdown([paper], "2026-07-17")
        self.assertIn("不代表课程推荐", rendered)
        self.assertIn("人工评审：待处理", rendered)
        self.assertIn(paper.url, rendered)


if __name__ == "__main__":
    unittest.main()
