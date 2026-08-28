# Changelog

## [Sprint 20] - JSON Validator

### Added

- Added `validate_json()` to validate JSON files.
- Added JSON Validator option to the JSON Tools menu.
- Added validation handling for valid and invalid JSON files.

### Changed

- Added error handling for missing files and unreadable JSON files.
- Added JSON syntax validation using Python's built-in `json` module.

## [Sprint 19] - JSON Formatter

### Added

- Added `json_tools.py` for JSON file processing.
- Added `read_json()` to read and parse JSON files.
- Added `write_json()` for reusable JSON output handling.
- Added `format_json()` to format JSON data with 4-space indentation.
- Added JSON Tools menu.
- Added JSON Formatter option to the JSON Tools menu.
- Integrated JSON Tools into the Main Menu.

### Changed

- Added error handling for missing files, invalid JSON, and JSON write errors.
- Added support for Unicode characters when formatting JSON.

## Sprint 18 - CSV Filter Column

### Added

- Added filter_column() to filter CSV data by a specific column value.
- Added case-insensitive column and value matching.
- Added CSV Filter Column option to the CSV Tools menu.

### Changed

- Added column selection and validation in the CSV menu.
- Added handling for invalid columns and unmatched filter values.

---

## Sprint 17 - CSV Search Data

### Added

- Added `search_data()` to search keywords across all CSV columns.
- Added case-insensitive keyword searching.
- Added CSV Search Data option to the CSV Tools menu.

### Changed

- Added validation for empty and whitespace-only search keywords.
- Improved error handling when the CSV file cannot be read.

---

## Sprint 16 - CSV Remove Duplicate Rows

### Added

- Added `remove_duplicate_rows()` to remove duplicate CSV rows.
- Added `write_csv()` for reusable CSV output handling.
- Added `get_rows_from_data()` to retrieve CSV data rows without the header.

### Changed

- Refactored CSV tools into I/O, analysis, and transformation sections.
- Updated CSV menu with the Remove Duplicates feature.

---

## Sprint 15 - Split CSV

### Added

- Added CSV split feature.
- Added streaming-based CSV processing to reduce memory usage.
- Added configurable rows per output file.
- Added automatic header preservation in each output file.
- Added support for remaining rows in the final output file.
- Added Split CSV option to the CSV Tools menu.

---

## Sprint 14 - Merge CSV

### Added

- Added `merge_csv()` function.
- Added header validation to ensure compatible CSV files.
- Added automatic `.csv` extension for output files.
- Added CSV file writing using Python's `csv.writer`.
- Added Merge CSV option to the CSV Tools menu.

---

## v0.5.0 - Sprint 13 - CSV Analyzer

### Added

- Added CSV tools module.
- Added CSV reader utility.
- Added row count feature.
- Added column count feature.
- Added CSV summary.
- Added CSV header reader.
- Added CSV preview feature.
- Added CSV menu.
- Integrated CSV menu into the main application.

---

## v0.4.0 - Sprint 12

### Added

- Added Count Lines tool.
- Added Count Words tool.
- Added File Size tool.
- Added File Analysis wrapper.
- Integrated File Analysis into File Menu.

---

## v0.3.0 - Sprint 11

### Added

- Added Main Menu.
- Added Text Menu.
- Added File Menu.
- Added menu navigation between application modules.

### Changed

- Refactored project structure into menu and tool layers.
- Main application now uses a centralized navigation flow.

---

## v0.2.0 - Sprint 10

### Added

- Added File Info tools.
- Check file existence.
- Get file name.
- Get file extension.
- Get absolute file path.

---

## v0.1.0 - Sprint 1–9

### Added

- Character Counter
- Word Counter
- Uppercase
- Lowercase
- Title Case
- Reverse Text
- Find & Replace
- Remove Duplicate Lines
- Sort Lines
