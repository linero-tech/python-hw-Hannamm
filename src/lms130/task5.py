def task5(items):
    result = [index * item for index, item in enumerate(items)]
    return result


if __name__ == "__main__":
    print("result is ", task5([1, 5, 11]))  # [0, 5, 22]
    print("result is ", task5([0, 0, 0, 0]))  # [0, 0, 0, 0]
    print("result is ", task5([-9, -9, 9, 1, 1, -9, 9, 3, 2, 2]))  # [0, -9, 18, 3, 4, -45, 54, 21, 16, 18]
    print("result is ", task5([1, 1, -2, 3, 4]))  # [0, 1, -4, 9, 16]
    print("result is ", task5([5, 6, 5, 6, 7, 8, 7]))  # [0, 6, 10, 18, 28, 40, 42]
