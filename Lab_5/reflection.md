# Lab 5 – Reflection

**Name:** Aryaman DK  **SRN:** PES1UG24AM344

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest were the Flake8 formatting issues (missing spaces, blank lines, a long line) and the missing docstrings. Each one points to an exact line and the fix is mechanical.

The hardest were the renames and the security fixes. Renaming `addService` to `add_service` and so on meant changing every call site in `main()` too, so one missed name would crash the program. For the MD5 warning I had to decide *why* MD5 was used: it only creates a short job-card id, so switching to SHA-256 would change the ids, while `usedforsecurity=False` keeps the behaviour and states the intent. Replacing `subprocess.call(..., shell=True)` also needed a different approach (`shutil.copy`), not just a small edit.

### 2. Did the static analysis tools report any false positives? If so, describe one example.

Yes, partly. Bandit B324 flagged `hashlib.md5()` as a "weak hash for security", but the code does not use it for security: it only makes an 8-character id for a job card. So the warning was a false positive in context. Instead of silencing it with `# nosec`, I added `usedforsecurity=False`, which documents the intent and satisfies Bandit.

Bandit B404 (importing `subprocess`) is also more of a "be careful" warning than a real bug: importing the module is not unsafe by itself. Here it went away once the real problem (B602, `shell=True`) was fixed.

### 3. How would you integrate static analysis tools into your actual software development workflow?

- **Locally:** run Flake8 and Pylint inside the editor (VS Code extensions) so problems show while typing, and add a `pre-commit` hook that runs Flake8, Pylint and Bandit before every commit.
- **In CI:** add a GitHub Actions workflow that runs all three tools on every push and pull request, and fails the build if Bandit finds a Medium/High issue, Flake8 finds any error, or the Pylint score drops below a set limit (for example 9.5).
- **Team rules:** keep a shared config (`.pylintrc`, `setup.cfg`) so everyone checks against the same rules, and only allow `# nosec` / `# pylint: disable` with a comment explaining why.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

- **Security:** the shell-injection risk in `backupRecords` is gone, and the password is no longer stored in the source code.
- **Correctness:** the mutable default list bug is fixed: before, every call to `addService` shared one `history` list; now each call gets its own. Catching only `KeyError` means real bugs are no longer hidden. The explicit UTF-8 encoding makes the JSON file behave the same on every OS, and the `__main__` guard stops the demo from running when the module is imported.
- **Readability:** consistent snake_case names and docstrings make each function's purpose clear without reading its body.
- **Measured result:** Pylint went from **4.66/10 to 10.00/10**, Bandit from **4 issues to 0**, Flake8 from **4 issues to 0**, and the program's output is unchanged.
