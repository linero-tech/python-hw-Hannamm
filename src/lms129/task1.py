#
def task1(a, b):
    result = 0

    for i in range(a, b + 1):
        if a >= b:
            result = 0
        else:
            result += i

    return result


if __name__ == "__main__":
    print("result is", task1(1, 5))
    print("result is", task1(3, 3))
    # print("result is", task1(2, 5))  # 12
    # print("result is", task1(1, 1))  # 0
    # print("result is", task1(3, 5))  # 12
    # print("result is", task1(4, 3))  # 0
    # print("result is", task1(4, 5))  # 9
    # print("result is", task1(9, 10))  # 19
