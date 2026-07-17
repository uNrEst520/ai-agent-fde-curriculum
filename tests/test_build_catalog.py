import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "docs" / "curriculum" / "catalog.json"
BUILDS = ROOT / "docs" / "builds" / "catalog.json"


class BuildCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = json.loads(CURRICULUM.read_text(encoding="utf-8-sig"))
        cls.builds = json.loads(BUILDS.read_text(encoding="utf-8-sig"))
        cls.modules = {module["id"]: module for module in cls.curriculum["modules"]}
        cls.projects = cls.builds["projects"]

    def test_every_module_has_exactly_one_build_project(self):
        project_modules = [project["module"] for project in self.projects]
        self.assertEqual(len(project_modules), len(set(project_modules)))
        self.assertEqual(set(project_modules), set(self.modules))

    def test_build_pages_have_six_or_more_milestones(self):
        for project in self.projects:
            with self.subTest(project=project["id"]):
                page = BUILDS.parent / project["page"]
                text = page.read_text(encoding="utf-8-sig")
                milestones = re.findall(r"^\| \d+\.", text, re.MULTILINE)
                self.assertGreaterEqual(len(milestones), 6)
                self.assertIn("## 通用验收", text)
                self.assertIn("## AI 使用规则", text)

    def test_module_and_build_pages_link_to_each_other(self):
        for project in self.projects:
            with self.subTest(project=project["id"]):
                module = self.modules[project["module"]]
                self.assertEqual(
                    module["build_page"],
                    f"../builds/{project['page']}",
                )
                module_page = CURRICULUM.parent / module["page"]
                module_text = module_page.read_text(encoding="utf-8-sig")
                self.assertIn(
                    f"(../../builds/{project['page']})",
                    module_text,
                )
                build_page = BUILDS.parent / project["page"]
                build_text = build_page.read_text(encoding="utf-8-sig")
                self.assertIn(f"[{project['module']}]", build_text)

    def test_build_index_links_every_project(self):
        index = (BUILDS.parent / "README.md").read_text(encoding="utf-8-sig")
        for project in self.projects:
            with self.subTest(project=project["id"]):
                self.assertIn(f"]({project['page']})", index)


if __name__ == "__main__":
    unittest.main()
