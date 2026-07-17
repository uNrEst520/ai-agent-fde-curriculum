import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs" / "resources" / "catalog.json"


class LearningResourceCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(CATALOG.read_text(encoding="utf-8-sig"))
        cls.resources = cls.data["resources"]

    def test_resource_ids_are_unique(self):
        ids = [resource["id"] for resource in self.resources]
        self.assertEqual(len(ids), len(set(ids)))

    def test_resources_have_actionable_metadata(self):
        required = {
            "id",
            "title",
            "provider",
            "kind",
            "url",
            "access",
            "role",
            "used_in",
            "required_scope",
            "estimated_minutes",
            "language",
            "last_verified",
        }
        for resource in self.resources:
            with self.subTest(resource=resource["id"]):
                self.assertTrue(required.issubset(resource))
                self.assertTrue(resource["url"].startswith("https://"))
                self.assertTrue(resource["used_in"])
                self.assertGreaterEqual(resource["estimated_minutes"], 0)

    def test_pilot_courses_do_not_link_search_result_pages(self):
        files = [
            ROOT / "docs" / "course" / "week-01" / "day-01-to-day-07.md",
            ROOT / "docs" / "curriculum" / "modules" / "00-learning-operating-system.md",
            ROOT / "docs" / "curriculum" / "modules" / "01-python-computational-thinking.md",
        ]
        for path in files:
            with self.subTest(path=path.name):
                self.assertNotIn(
                    "youtube.com/results",
                    path.read_text(encoding="utf-8-sig"),
                )

    def test_phase_one_has_primary_resources(self):
        used_by_module = {
            module: [
                resource
                for resource in self.resources
                if module in resource["used_in"] and resource["role"] == "primary"
            ]
            for module in ("O00", "SE01-W1", "SE01-W2", "SE01-W3", "SE01-W4", "SE01-W5", "SE01-W6")
        }
        for module, resources in used_by_module.items():
            with self.subTest(module=module):
                self.assertTrue(resources)

    def test_se01_trains_ai_assisted_code_review_not_blank_page_coding(self):
        module = (
            ROOT
            / "docs"
            / "curriculum"
            / "modules"
            / "01-python-computational-thinking.md"
        ).read_text(encoding="utf-8-sig")
        build = (ROOT / "docs" / "builds" / "cli-data-app.md").read_text(
            encoding="utf-8-sig"
        )

        for required in (
            "不要求从空白文件手写完整应用",
            "预测行为、作出判断、验收结果",
            "逻辑错误",
            "Codex 补丁",
        ):
            with self.subTest(required=required):
                self.assertIn(required, module)

        self.assertIn("代码审阅与逻辑验证档案", build)
        self.assertIn("三类必做逻辑故障", build)
        self.assertNotIn("至少 30 个", module)
        self.assertNotIn("从空目录或最小脚手架开始", build)

    def test_se01_official_agent_python_references_are_cataloged(self):
        by_id = {resource["id"]: resource for resource in self.resources}
        for resource_id in (
            "PYDANTIC-MODELS",
            "PYTHON-ASYNCIO-TASKS",
            "MS-LANGCHAIN-BEGINNERS",
        ):
            with self.subTest(resource_id=resource_id):
                self.assertIn(resource_id, by_id)
                self.assertIn("SE01-W5", by_id[resource_id]["used_in"])


if __name__ == "__main__":
    unittest.main()
