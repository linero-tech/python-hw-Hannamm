

def task10_1(assessments):
    result = len(assessments)
    return result


if __name__ == "__main__":
    print("result is", task10_1("LMHHF"))


def task10_2(assessments):
    minute = 4 - 1
    result = assessments[minute]
    return result


if __name__ == "__main__":
    print("result is", task10_2("LMFHMF"))


def task10_3(assessments):
    midpoint = len(assessments) // 2
    result = assessments[midpoint]
    return result


if __name__ == "__main__":
    print("result is", task10_3("LMFHM"))


def task10_4(assessments):
    result = assessments[:3]
    return result


if __name__ == "__main__":
    print("result is", task10_4("LMFHM"))

