"""
Lab 7 - Fuzz Testing (Fixed Application)
Name : Aryaman D K
SRN  : PES1UG24AM344
Repo : L6_L7_39_password_policy

Hardened version of password_policy.py. Every function now validates its
input first, so the edge cases found by Hypothesis (None, empty strings,
missing or extra ':' separators) no longer crash the program.
"""


def first_character_type(pw):
    """Return 'digit', 'letter' or 'symbol' for the first character.

    Invalid input (None / non-string) -> 'invalid'
    Empty string                      -> 'empty'
    """
    if not isinstance(pw, str):          # Bug fix: None raised TypeError
        return 'invalid'
    if len(pw) == 0:                     # Bug fix: '' raised IndexError
        return 'empty'

    ch = pw[0]
    if ch.isdigit():
        return 'digit'
    if ch.isalpha():
        return 'letter'
    return 'symbol'


def split_credentials(text):
    """Split 'user:password' into (user, password).

    Returns None when the input is not a valid 'user:password' string.
    """
    if not isinstance(text, str):        # Bug fix: None raised AttributeError
        return None
    if ':' not in text:                  # Bug fix: '' / no ':' raised ValueError
        return None

    # Bug fix: split only on the FIRST ':' so passwords may contain ':'
    user, password = text.split(':', 1)
    user, password = user.strip(), password.strip()

    if user == '' or password == '':     # reject ':pass', 'user:' and ':'
        return None
    return user, password


def digit_ratio(pw):
    """Return the fraction of characters in pw that are digits (0.0 to 1.0).

    Invalid input (None / non-string) or an empty string -> 0.0
    """
    if not isinstance(pw, str):          # Bug fix: None raised TypeError
        return 0.0
    if len(pw) == 0:                     # Bug fix: '' raised ZeroDivisionError
        return 0.0
    return sum(c.isdigit() for c in pw) / len(pw)


def main():
    print("==== Running first_character_type ====")
    user_input = input("Enter a password: ")
    result = first_character_type(user_input)
    if result == 'empty':
        print("First Character Type: Error - password cannot be empty")
    else:
        print("First Character Type:", result)

    print("\n==== Running split_credentials ====")
    user_input = input("Enter user:password (e.g. alice:Secret1): ")
    result = split_credentials(user_input)
    if result is None:
        print("User and Password: Error - expected format user:password")
    else:
        print("User and Password:", result)

    print("\n==== Running digit_ratio ====")
    user_input = input("Enter a password to measure: ")
    result = digit_ratio(user_input)
    print("Digit Ratio:", result)


if __name__ == "__main__":
    main()
