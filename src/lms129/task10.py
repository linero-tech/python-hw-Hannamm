import re


def task10(password):

    # Define the regular expression pattern for password validation
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,10}$"

    # Compile the pattern into a regular expression object
    regex = re.compile(pattern)

    # Check if the password matches the regular expression pattern
    if regex.match(password):
        result = True

    else:
        result = False
    return result


if __name__ == "__main__":
    print(task10("Ani2#"))  # Minimum length 6 characters
    print(task10("Animate2111111#"))  # Maximum length 10 characters
    print(task10("ANIMATE21@"))  # At least 1 letter between [a-z]
    print(task10("ani222#"))  # At least 1 letter between [A-Z].
    print(task10("Animate#"))  # At least 1 number between [0-9].
    print(task10("Animate2"))  # At least 1 of the following character [$#@].
    print(task10("Animate4@"))  # Password is valid
