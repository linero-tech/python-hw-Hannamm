from to_do import TODO


def task2(items):
    result = 0

    if items:  # check if items is not empty
        for i in range(0, len(items), 2):
            result += items[i]
    else:
        result = 0

    return result


if __name__ == "__main__":
    print("result is ", task2([]))  # 0
    print("result is ", task2([1, 2, 3, 4]))  # 4
    print("result is ", task2([1, 2]))  # 1
    print("result is ", task2([5, 7, 9]))  # 14
    print("result is ", task2([1, 1, -2, 3, 4]))  # 3
    print("result is ", task2([0, 1, 2, 3, 4, 5]))  # 6
    print("result is ", task2([8, 9, 0, 6, 3, 6, 8, 4, 6, 456, 3, 5, 3, 7, 4, 5566, 234, 1, 234, 35646, 234]))  # 737
