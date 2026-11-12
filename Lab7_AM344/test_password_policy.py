"""
Lab 7 - Fuzz Testing with Hypothesis
Name : Aryaman D K
SRN  : PES1UG24AM344
Repo : L6_L7_39_password_policy

Property-based fuzz tests for password_policy.py.
Hypothesis generates random / unexpected inputs (Unicode text, empty
strings, None) to check that every function behaves safely.
"""

from hypothesis import given, settings, strategies as st
from password_policy import first_character_type, split_credentials, digit_ratio


# ---------------------------------------------------------------
# 1. first_character_type
# ---------------------------------------------------------------

@given(st.text() | st.none())
def test_first_character_type_no_crash(s):
    """Property: must never raise, whatever the input."""
    try:
        first_character_type(s)
    except Exception as e:
        assert False, f"first_character_type crashed with: {e!r} on input {s!r}"


@given(st.text(min_size=1))
def test_first_character_type_valid_label(s):
    """Property: for any non-empty string the result is one of the known labels."""
    assert first_character_type(s) in {"digit", "letter", "symbol"}


# ---------------------------------------------------------------
# 2. split_credentials
# ---------------------------------------------------------------

@given(st.text() | st.none())
def test_split_credentials_no_crash(s):
    """Property: must never raise, whatever the input."""
    try:
        split_credentials(s)
    except Exception as e:
        assert False, f"split_credentials crashed with: {e!r} on input {s!r}"


@given(
    st.text(alphabet=st.characters(blacklist_characters=":"), min_size=1)
      .filter(lambda u: u.strip() != ""),
    # password alphabet deliberately includes ':' so the fuzzer tries it often
    st.text(alphabet="abcXYZ123!@# :", min_size=1).filter(lambda p: p.strip() != ""),
)
def test_split_credentials_round_trip(user, password):
    """Property: 'user:password' is split back into (user, password),
    even when the password itself contains ':' characters."""
    assert split_credentials(f"{user}:{password}") == (user.strip(), password.strip())


# ---------------------------------------------------------------
# 3. digit_ratio
# ---------------------------------------------------------------

@given(st.text() | st.none())
def test_digit_ratio_no_crash(s):
    """Property: must never raise, whatever the input."""
    try:
        digit_ratio(s)
    except Exception as e:
        assert False, f"digit_ratio crashed with: {e!r} on input {s!r}"


@given(st.text())
def test_digit_ratio_in_range(s):
    """Property: the ratio is always a number between 0 and 1."""
    assert 0.0 <= digit_ratio(s) <= 1.0
