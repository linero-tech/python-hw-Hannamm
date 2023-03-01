import re


def task10(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,10}$"
    if re.match(pattern, password):
        result = "Valid password"
    else:
        result = "Invalid password"

    return result


if __name__ == "__main__":
    print(task10("Animate2#"))  # Valid Password
    print(task10("Animate211#"))  # Not Valid Password
    print(task10("ani21@"))  # Not Valid Password
    print(task10("Ani222"))  # Not Valid Password
