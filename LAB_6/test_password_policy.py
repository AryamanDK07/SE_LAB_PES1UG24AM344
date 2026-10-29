
import pytest
from password_policy import check_password, strength, suggest_fix


# Code coverage: check_password()

def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []


def test_password_too_short():
    assert "too short" in check_password("Ab1!")


def test_password_too_long():
    assert "too long" in check_password("Ab1!" + "x" * 62)


def test_common_password():
    assert "common" in check_password("password")


def test_common_password_case_insensitive():
    assert "common" in check_password("PASSWORD")


def test_missing_uppercase():
    assert "no uppercase" in check_password("abcdef1!")


def test_missing_lowercase():
    assert "no lowercase" in check_password("ABCDEF1!")


def test_missing_digit():
    assert "no digit" in check_password("Abcdefgh!")


def test_missing_special():
    assert "no special" in check_password("Abcdef12")


def test_password_exactly_8_characters():
    assert check_password("Abcdef1!") == []


def test_password_exactly_64_characters():
    assert check_password("A" + "a" * 61 + "1!") == []


# Code coverage: strength()

def test_valid_password_is_good():
    assert strength("Abcdef1!") == "good"


def test_long_valid_password_is_strong():
    assert strength("Abcdefghij1!xy") == "strong"


def test_invalid_password_is_weak():
    assert strength("Ab1!") == "weak"


def test_invalid_password_is_very_weak():
    assert strength("a") == "very weak"


# Code coverage: suggest_fix()

def test_no_fix_needed():
    assert suggest_fix([]) == "none needed"


def test_suggest_fix_short():
    assert suggest_fix(["too short"]) == "add more characters"


def test_suggest_fix_common():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_suggest_fix_missing_digit():
    assert suggest_fix(["no digit"]) == "add digit"


def test_suggest_fix_missing_uppercase():
    assert suggest_fix(["no uppercase"]) == "add uppercase"


def test_suggest_fix_too_long():
    assert suggest_fix(["too long"]) == "shorten it"


def test_first_issue_is_used():
    assert suggest_fix(["too short", "no digit"]) == "add more characters"
