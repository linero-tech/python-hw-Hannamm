def task9(items):
    result = []

    if items:
        result.append(items[0] ** 2)  # multiply the first element by itself
        for i in range(1, len(items)):
            result.append(items[i] * items[i - 1])  # multiply each element by the previous element
    else:
        result = []

    return result


if __name__ == "__main__":
    print("result is ", task9([5, 2, 3, 4]))  # [25, 10, 6, 12]
    print("result is ", task9([9, 1, 2, 3, 6]))  # [81, 9, 2, 6, 18]
    print("result is ", task9([4]))  # [16]
    print("result is ", task9([1, -2, 3, -4]))  # [1, -2, -6, -12]
    print("result is ", task9([]))  # []
    print("result is ", task9([0, 1, 0, 1]))  # [0, 0, 0, 0]
    print("result is ", task9([1, 1, 1, 1]))  # [1, 1, 1, 1]
