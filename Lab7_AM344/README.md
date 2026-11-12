# Lab 7 – Fuzzing for Input Validation Bugs

**Name:** Aryaman D K
**SRN:** PES1UG24AM344
**Assigned repo:** L6_L7_39_password_policy (lab7)

## Files

| File | Description |
|------|-------------|
| `password_policy.py` | Fixed (hardened) application script |
| `test_password_policy.py` | Completed Hypothesis fuzz tests |
| `Lab7_AM344_Report.pdf` | Report with screenshots for every step |
| `screenshots/` | Individual screenshots used in the report |

## How to run

```
pip install hypothesis pytest
python password_policy.py
python -m pytest test_password_policy.py -v
```

## Bugs found by fuzzing and fixed

| Function | Failing input | Error | Fix |
|----------|---------------|-------|-----|
| `first_character_type` | `''` | IndexError | returns `'empty'` |
| `first_character_type` | `None` | TypeError | returns `'invalid'` |
| `split_credentials` | `''`, `'alice'` | ValueError | returns `None` when `:` is missing |
| `split_credentials` | `None` | AttributeError | returns `None` for non-strings |
| `split_credentials` | `'0::'` | ValueError | splits only on the first `:` |
| `split_credentials` | `':'`, `'user:'` | empty parts returned | returns `None` |
| `digit_ratio` | `''` | ZeroDivisionError | returns `0.0` |
| `digit_ratio` | `None` | TypeError | returns `0.0` |

Before fix: **5 failed, 1 passed** · After fix: **6 passed**
