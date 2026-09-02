# Output modes and preference handling

## Resolution order

Choose the output destination in this order:

1. an existing spreadsheet that the user explicitly asked to update;
2. a format or destination explicitly selected for the current task;
3. a previously saved itinerary-output preference;
4. a portable Microsoft Excel `.xlsx` workbook as the default.

An explicit target for the current task overrides a saved preference. Do not create duplicate output merely to satisfy the saved preference.

## Existing cloud spreadsheet

When the user provides an existing Google Sheets, Excel Online, or other cloud-spreadsheet target:

1. attempt a read-only metadata or range read using an already authorized connector;
2. confirm whether the available access is read-only or writable;
3. edit in place only when the request calls for modification and write access is available;
4. if access is insufficient, explain the exact access limitation and offer normal document sharing or an `.xlsx` export;
5. never request credentials, authentication codes, tokens, or secret links in chat.

If the user supplied the spreadsheet only as a visual reference, do not assume authorization to overwrite it.

## New Google Sheets output

Create a new Google Sheets document only when the user selects it, a saved preference selects it, or the surrounding workflow clearly requires a shareable cloud sheet and the necessary connector is available. Report the created destination without exposing unrelated account details.

If the connector cannot create the document, fall back to `.xlsx` unless the user specifically requires Google Sheets; in that case, report the blocker and request a normal connector or sharing setup.

## Microsoft Excel output

Use `.xlsx` as the portable default when there is no existing target, current-task choice, or saved preference. Preserve formulas, merges, widths, colors, wrapping, frozen panes, and print settings when the available workbook tool supports them.

State that the output is an Excel-compatible `.xlsx` file; do not imply that the Microsoft Excel application or a Microsoft 365 account is required.

## CSV fallback

Use CSV only when the user requests it or no richer spreadsheet format is available. Warn that CSV cannot preserve merged cells, exact widths, colors, formulas, multiple sheets, frozen panes, or print settings. A CSV result is a data fallback, not a complete implementation of the canonical layout.

## Preference persistence

- A statement such as "use Excel this time" is task-scoped and must not change the saved default.
- A statement such as "always use Excel for future itineraries" may be saved as the itinerary-output preference when the platform supports memory.
- Persist only the output type by default, such as `google-sheets` or `xlsx`.
- Do not persist private spreadsheet URLs, file IDs, account identifiers, or sharing targets unless the user explicitly asks to use a specific document as a future template.
- If persistent memory is unavailable, apply the choice to the current task and state that it could not be saved for future sessions.
