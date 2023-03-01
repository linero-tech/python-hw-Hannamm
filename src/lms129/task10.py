def task10(password):
    import re

    result = f"The password '{password}' is valid but you indicated otherwise."

    if len(password) < 6:
        result = f"The password '{password}' is invalid: It has less than 6 characters."

    if len(password) > 10:
        result = f"The password '{password}' is invalid: It has more than 10 characters"

    if not re.search("[a-z]", password):
        result = f"The password '{password}' is invalid: It is missing at least one lowercase character."

    if not re.search("[A-Z]", password):
        result = f"The password '{password}' is invalid: It is missing at least one uppercase character."

    if not re.search("[0-9]", password):
        result = f"The password '{password}' is invalid: It is missing at least one number."

    if not re.search("[$#@]", password):
        result = f"The password '{password}' is invalid: It is missing at least one of the special characters"

    return result


if __name__ == "__main__":
    print(task10("Ani2#"))  # Minimum length 6 characters
    print(task10("Animate2111111#"))  # Maximum length 10 characters
    print(task10("ANIMATE21@"))  # At least 1 letter between [a-z]
    print(task10("ani222#"))  # At least 1 letter between [A-Z].
    print(task10("Animate#"))  # At least 1 number between [0-9].
    print(task10("Animate2"))  # At least 1 of the following character [$#@].
    print(task10("Animate4@"))  # Password is valid
