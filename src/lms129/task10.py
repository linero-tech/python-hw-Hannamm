import re


def task10(password):
    result = True

    if len(password) < 6 or len(password) > 10:
        result = False
    elif not re.search("[a-z]", password):
        result = False

    elif not re.search("[0-9]", password):
        result = False

    elif not re.search("[A-Z]", password):
        result = False

    elif not re.search("[$#@]", password):
        result = False

    if result:
        result = "Valid Password"
    else:
        result = "Not Valid Password"

    return result


if __name__ == "__main__":
    print(task10("Animate2#"))  # Valid Password
    print(task10("Animate211#"))  # Not Valid Password
    print(task10("ani21@"))  # Not Valid Password
    print(task10("Ani222"))  # Not Valid Password
