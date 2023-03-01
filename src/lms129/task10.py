def task10(password):
    import re

    result = "The password is Valid"

    if len(password) < 6:
        result = "The password is invalid: It has less than 6 characters."

    if len(password) > 10:
        result = "The password is invalid: Password must be at most 10 characters long. "

    if not re.search("[a-z]", password):
        result = "The password is invalid: Password must contain at least one lowercase letter. "

    if not re.search("[A-Z]", password):
        result = "The password is invalid: Password must contain at least one uppercase letter. "

    if not re.search("[0-9]", password):
        result = "The password is invalid: Password must contain at least one digit. "

    if not re.search("[$#@]", password):
        result = "The password is invalid: Password must contain at least one of the following characters: $, #, @. "

    return result


if __name__ == "__main__":
    print(task10("Ani2#"))  # Minimum length 6 characters
    print(task10("Animate2111111#"))  # Maximum length 10 characters
    print(task10("ANIMATE21@"))  # At least 1 letter between [a-z]
    print(task10("ani222#"))  # At least 1 letter between [A-Z].
    print(task10("Animate#"))  # At least 1 number between [0-9].
    print(task10("Animate2"))  # At least 1 of the following character [$#@].
    print(task10("Animate4@"))  # Password is valid
