import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs" / "curriculum" / "catalog.json"


class CurriculumCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(CATALOG.read_text(encoding="utf-8-sig"))
        cls.modules = cls.data["modules"]

    def test_program_has_nineteen_core_and_twelve_electives(self):
        core = [module for module in self.modules if module["stage"] != "elective"]
        electives = [module for module in self.modules if module["stage"] == "elective"]
        self.assertEqual(len(core), 19)
        self.assertEqual(len(electives), 12)
        self.assertEqual(len(self.modules), 31)

    def test_module_ids_are_unique(self):
        module_ids = [module["id"] for module in self.modules]
        self.assertEqual(len(module_ids), len(set(module_ids)))

    def test_all_pages_exist_and_are_linked_from_readme(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")
        for module in self.modules:
            with self.subTest(module=module["id"]):
                page = CATALOG.parent / module["page"]
                self.assertTrue(page.is_file())
                self.assertIn(f"(docs/curriculum/{module['page']})", readme)

    def test_prerequisites_refer_to_known_modules(self):
        known = {module["id"] for module in self.modules}
        for module in self.modules:
            with self.subTest(module=module["id"]):
                self.assertTrue(set(module["prerequisites"]).issubset(known))
                self.assertNotIn(module["id"], module["prerequisites"])

    def test_declared_core_duration_matches_catalog(self):
        core_weeks = sum(
            module["duration_weeks"]
            for module in self.modules
            if module["stage"] != "elective"
        )
        self.assertEqual(self.data["core_estimated_weeks"], core_weeks)
        self.assertEqual(core_weeks, 108)


if __name__ == "__main__":
    unittest.main()
