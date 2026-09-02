---
name: travel-itinerary-spreadsheet-format
description: Create, fill, review, or normalize a detailed travel itinerary spreadsheet using a consistent 12-column A4 landscape layout, exact column widths, daily date grouping, cost formulas, and verification checks. Use when the requested output is an itinerary spreadsheet or an existing trip sheet needs layout and content cleanup.
license: MIT
---

# Travel Itinerary Spreadsheet Format

## 1. Inspect the target

- Determine whether the task creates a new itinerary or updates an existing spreadsheet.
- Read available values, formulas, merges, formatting, column widths, frozen rows, and print settings before editing.
- Preserve intentional user edits and identify facts that require later confirmation, such as future schedules, fares, business hours, or booking rules.
- If the spreadsheet tool cannot inspect or apply a required property, state that limitation instead of claiming it was verified.

**Done when:** the current structure, editable scope, preserved choices, and verification limitations are known.

## 2. Apply the canonical schema

- Use exactly the 12 columns and widths in [`references/layout-spec.md`](references/layout-spec.md).
- Keep reservation guidance and reservation links together in one column.
- Place reservation information between meal recommendations and dining tips.
- Keep itinerary rows focused on the actual schedule; add separate summary blocks only when requested.

**Done when:** every itinerary row maps cleanly to the canonical 12-column order with no duplicate or obsolete columns.

## 3. Fill practical itinerary content

- Include useful transportation, area, place, food candidates, booking guidance, operational notes, estimated cost, and booking status where applicable.
- Put reservation advice and related URLs together. Use one URL per line when multiple links are needed.
- Distinguish official sources from third-party booking pages.
- Flag cancellation rules and time-sensitive facts that must be checked again near departure.

**Done when:** each scheduled row contains enough information for a traveler to act without mixing unrelated planning notes into the timetable.

## 4. Apply layout and styling

- Follow the print, typography, alignment, color, border, wrapping, and freezing rules in [`references/layout-spec.md`](references/layout-spec.md).
- Preserve consistent spacing and do not estimate widths when the tool can apply exact pixel values.
- Group repeated dates vertically and keep the time-of-day column immediately after the date.

**Done when:** the sheet is readable on screen and fits sensibly across A4 landscape pages without forcing all rows onto one page vertically.

## 5. Apply formulas and data rules

- Store numeric costs as numbers and format them as currency.
- Calculate the final total with a `SUM` formula rather than typing a fixed result.
- Preserve valid formulas and booking-status controls in an existing sheet.

**Done when:** currency cells are numeric where possible, the total is formula-driven, and editing controls remain usable.

## 6. Verify the result

Read the finished sheet back and check:

1. column order and exact widths;
2. values, formulas, merges, wrapping, alignment, borders, and frozen row;
3. date weekdays and daily merge ranges;
4. missing or duplicate itinerary rows;
5. URLs and source labels;
6. booking, fare, schedule, and business-hour caveats;
7. currency formatting and total formula;
8. landscape print settings and obvious typographical errors.

Use [`examples/sample-itinerary.csv`](examples/sample-itinerary.csv) only as a structural example, not as factual travel advice.

**Done when:** all supported checks pass and the final report lists changes, unresolved facts, and tool limitations.
