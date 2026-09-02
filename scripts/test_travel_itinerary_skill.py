import csv
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "travel-itinerary-spreadsheet-format"

EXPECTED_COLUMNS = [
    ("A", "日期", 61),
    ("B", "時段", 51),
    ("C", "主交通方式", 109),
    ("D", "主要區域", 115),
    ("E", "地點", 203),
    ("F", "推薦美食", 136),
    ("G", "類型／推薦餐點", 133),
    ("H", "訂位建議／訂位連結", 268),
    ("I", "用餐提示／重點特色", 201),
    ("J", "備註", 286),
    ("K", "費用", 105),
    ("L", "成行", 91),
]


class TravelItinerarySkillContractTests(unittest.TestCase):
    def test_layout_table_preserves_columns_and_widths(self) -> None:
        text = (SKILL_DIR / "references" / "layout-spec.md").read_text(encoding="utf-8")
        rows = re.findall(
            r"\| ([A-L]) \| ([^|]+?) \| (\d+) px \|",
            text,
        )
        actual = [(letter, header.strip(), int(width)) for letter, header, width in rows]
        self.assertEqual(actual, EXPECTED_COLUMNS)

    def test_sample_uses_canonical_header(self) -> None:
        path = SKILL_DIR / "examples" / "sample-itinerary.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
        self.assertEqual(rows[0], [header for _, header, _ in EXPECTED_COLUMNS])
        self.assertTrue(all(len(row) == 12 for row in rows))

    def test_workflow_retains_required_behaviors(self) -> None:
        skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        layout = (SKILL_DIR / "references" / "layout-spec.md").read_text(encoding="utf-8")
        combined = skill + "\n" + layout
        required_phrases = [
            "Preserve intentional user edits",
            "Keep reservation guidance and reservation links together",
            "transit or sightseeing passes",
            "Merge the date cells vertically",
            "A4",
            "landscape",
            "Freeze: first row",
            "`SUM` formula",
            "facts that require later confirmation",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)


if __name__ == "__main__":
    unittest.main()
