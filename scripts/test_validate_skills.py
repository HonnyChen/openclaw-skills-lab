import tempfile
import unittest
from pathlib import Path

from validate_skills import validate_skill


class ValidateSkillTests(unittest.TestCase):
    def test_valid_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill_dir = Path(directory) / "demo-skill"
            skill_dir.mkdir()
            (skill_dir / "reference.md").write_text("ok\n", encoding="utf-8")
            (skill_dir / "SKILL.md").write_text(
                "---\nname: demo-skill\ndescription: A demo.\n---\n"
                "\nRead [reference](reference.md).\n",
                encoding="utf-8",
            )
            self.assertEqual(validate_skill(skill_dir), [])

    def test_broken_reference(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill_dir = Path(directory) / "demo-skill"
            skill_dir.mkdir()
            (skill_dir / "SKILL.md").write_text(
                "---\nname: demo-skill\ndescription: A demo.\n---\n"
                "\nRead [missing](missing.md).\n",
                encoding="utf-8",
            )
            self.assertTrue(any("broken local reference" in error for error in validate_skill(skill_dir)))


if __name__ == "__main__":
    unittest.main()
