# Layout specification

## Column order and widths

| Column | Header | Width |
| --- | --- | ---: |
| A | 日期 | 61 px |
| B | 時段 | 51 px |
| C | 主交通方式 | 109 px |
| D | 主要區域 | 115 px |
| E | 地點 | 203 px |
| F | 推薦美食 | 136 px |
| G | 類型／推薦餐點 | 133 px |
| H | 訂位建議／訂位連結 | 268 px |
| I | 用餐提示／重點特色 | 201 px |
| J | 備註 | 286 px |
| K | 費用 | 105 px |
| L | 成行 | 91 px |

If a spreadsheet editor uses non-pixel width units, preserve the ratios above and verify the exported page instead of claiming exact pixel equivalence.

## Print settings

- Paper: A4
- Orientation: landscape
- Horizontal alignment: centered
- Gridlines: visible
- Left and right margins: 0.25 inch
- Top and bottom margins: 0.75 inch
- Header and footer margins: 0
- Scale: fit to width sensibly; do not fit all rows to one page vertically
- Freeze: first row

## Daily date grouping

- Put a date in the first itinerary row for that day.
- Merge the date cells vertically across all rows belonging to that day.
- Center and bold the merged date cell.
- Keep `時段` immediately after `日期`.

## Styling

- Header: bold, centered, wrapped, vertically centered, consistent blue fill, and borders.
- Body: Arial 12, wrapped, vertically centered, and bordered.
- Center these columns: date, time, transportation, area, cost, and booking status.
- Place names: food in bold brown; attractions, shopping, and sightseeing in bold light green; accommodation in bold blue.
- Notes: time-critical, ticket, reservation, crowd, deadline, and airport reminders in bold red; ordinary notes in black.
- Preserve merged daily date cells and the merged total label.
- Numeric costs use the requested currency format; the final total uses a `SUM` formula.
