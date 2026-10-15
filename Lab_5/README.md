# Lab 5: Static Code Analysis — Vehicle Service Management System

**Name:** Aryaman DK
**SRN:** PES1UG24AM344
**Assigned repo:** [SETAPESU26/L5_39_vehicle_service](https://github.com/SETAPESU26/L5_39_vehicle_service)

Static analysis of `vehicle_service.py` using **Pylint**, **Bandit** and **Flake8**, then fixing every reported issue.

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.66 / 10 | **10.00 / 10** |
| Bandit | 4 issues (2 High, 2 Low) | **0 issues** |
| Flake8 | 4 issues | **0 issues** |

Program output is identical before and after the fixes (`reports/program_output.txt`).

## Files

| File | Contents |
|------|----------|
| `vehicle_service.py` | Cleaned, fixed script |
| `issues.md` | Issue table (14 issues: tool code, type, lines, description, fix) |
| `reflection.md` | Answers to the four reflection questions |
| `reports/before/` | `pylint_report.txt`, `bandit_report.txt`, `flake8_report.txt` on the original code |
| `reports/after/` | The same three reports on the fixed code |
| `reports/program_output.txt` | Output of `python vehicle_service.py` |

## Commits for the fixes (one per tool)

1. **Fix Bandit security issues** — B602 shell=True, B324 MD5, B105 hardcoded password, B404 subprocess import
2. **Fix Flake8 style issues** — E231, E225, E302, E501
3. **Fix Pylint issues** — mutable default arg, broad except, open() encoding, snake_case names, docstrings, `__main__` guard

## How to reproduce

```
python3 -m venv venv
source venv/bin/activate
pip install pylint bandit flake8
python vehicle_service.py
pylint vehicle_service.py > pylint_report.txt
bandit -r vehicle_service.py > bandit_report.txt
flake8 vehicle_service.py > flake8_report.txt
```
