# Update Script Maintenance Report

Date: 2026-03-03

- Ran the update pipeline (`make all`) and diagnosed parser/runtime failure.
- Root cause: `xlrd==1.2.0` path was incompatible in this environment for workbook parsing.
- Updated parser in `scripts/process.py` to use `pandas.read_excel` with robust date parsing.
- Added guarded processing so failures are surfaced per source file.
- Updated dependencies in `requirements.txt` to modern Excel stack.
- Added `permissions: contents: write` in `.github/workflows/update.yml` for reliable scheduled pushes.
