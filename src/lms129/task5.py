from to_do import TODO


def task5(sentence):
    result = 0

    for _ in sentence:
        result += 1
    return result


if __name__ == "__main__":
    print("result is ", task5("I love GBG"))
