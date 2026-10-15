# Lab 5 – Identified Issues: `vehicle_service.py`

**Name:** Aryaman DK  **SRN:** PES1UG24AM344
**Repo assigned:** SETAPESU26/L5_39_vehicle_service

Line numbers refer to the **original** file (see `reports/before/`). Rows are ordered by severity: high and medium first.

| # | Issue | Type | Line(s) | Description | Fix Approach |
|---|-------|------|---------|-------------|--------------|
| 1 | Shell injection – Bandit **B602** (High) | Security | 61 | `subprocess.call("cp services.json " + folder, shell=True)` builds a shell command from user input. A folder name like `x; rm -rf ~` would run extra commands. | Removed `subprocess` entirely and used `shutil.copy("services.json", folder)`, which copies the file in Python with no shell involved. |
| 2 | Weak MD5 hash – Bandit **B324** (High) | Security | 39 | `hashlib.md5()` is flagged because MD5 is broken for security use. | The hash is only used to make a short job-card id, not for security, so passed `usedforsecurity=False`. This tells Python (and Bandit) the intent and keeps the same ids (`353ee89f`). |
| 3 | Mutable default argument – Pylint **W0102** | Bug | 12 | `history=[]` is created once and shared by every call, so bookings from earlier calls leak into later ones. | Changed default to `history=None` and create a new list inside the function (`if history is None: history = []`). |
| 4 | Broad exception – Pylint **W0718** | Bug | 23 | `except Exception:` hides every error (typos, bugs), not just "vehicle not found". | Catch only `KeyError`, the one error expected when a vehicle has no records. |
| 5 | Open without encoding – Pylint **W1514** | Bug | 50 | `open(fileName, "w")` uses the system default encoding, so the file may be written and read differently on Windows vs Linux. | Added `encoding="utf-8"` (matches `loadRecords`, which already used it). |
| 6 | Hardcoded password – Bandit **B105** (Low) | Security | 8 | `ADMIN_PASSWORD = "garage-demo"` puts a secret in the source code and in Git history. | Read it from an environment variable: `os.environ.get("GARAGE_ADMIN_PASSWORD", "")`. |
| 7 | subprocess import – Bandit **B404** (Low) | Security | 3 | Importing `subprocess` is flagged as a possible command-execution risk. | Import removed (no longer needed after fix #1). |
| 8 | Non-snake_case names – Pylint **C0103** | Style | 12, 20, 31, 32, 34, 38, 42, 49, 54, 59 | `addService`, `vehicleNo`, `totalCost`, `fileName` etc. break the PEP 8 naming convention. | Renamed to `add_service`, `vehicle_no`, `total_cost`, `file_name`, etc., and updated every call in `main()`. |
| 9 | Missing docstrings – Pylint **C0114 / C0116** | Style | 1, 12, 20, 31, 38, 42, 49, 54, 59, 64 | No module docstring and no function docstrings. | Added a module docstring and a one-line docstring to every function. |
| 10 | Missing whitespace after comma – Flake8 **E231** | Style | 7 | `2500,"Brake Check"` | Added a space: `2500, "Brake Check"`. |
| 11 | Missing whitespace around operator – Flake8 **E225** | Style | 43 | `best=None` | Changed to `best = None`. |
| 12 | Expected 2 blank lines – Flake8 **E302** | Style | 49 | Only one blank line before `def saveRecords`. | Added the second blank line. |
| 13 | Line too long – Flake8 **E501** | Style | 77 | Print line was 83 characters (limit 79). | Wrapped the `print(...)` call over two lines. |
| 14 | `main()` runs on import | Bug (found by review) | 79 | `main()` was called at module level, so just importing the file ran the demo and wrote `services.json`. | Wrapped in `if __name__ == "__main__":`. |

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.66 / 10 (31 messages) | **10.00 / 10** (0 messages) |
| Bandit | 4 issues (2 High, 2 Low) | **No issues identified** |
| Flake8 | 4 issues | **0 issues** |

The program prints exactly the same output before and after the fixes (see `reports/program_output.txt`).
