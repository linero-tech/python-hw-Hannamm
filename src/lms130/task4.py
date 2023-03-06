
def task4(items, factor):

    result = list(set([item for item in items if item % factor == 0]))

    return result


if __name__ == "__main__":
    print("result is ", task4([], 2))  # []
    print("result is ", task4([1, 2, 4, 5, 6], 2))  # [2, 4, 6]
    print("result is ", task4([0, 0, 0, 0], 2))  # [0]
    print("result is ", task4([-9, -9, 9, 1, 1, -9, 9, 3, 2, 2], 3))  # [2]
    print("result is ", task4([1, 1, -2, 3, 4], 4))  # [4, -2]
    print("result is ", task4([5, 6, 5, 6, 7, 8, 7], 5))  # [8, 6]
