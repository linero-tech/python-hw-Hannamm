def task8(items):
    result = []

    # Sort the list in ascending order
    items.sort()

    # Get the last three elements
    result = items[-3:]

    # Reverse the order to get ascending order

    return result


if __name__ == "__main__":
    print("result is ", task8([60, 9, 7, 10]))  # [9, 10, 60]
    print("result is ", task8([1, 2, 3, 4, 5]))  # [3, 4, 5]
    print("result is ", task8([4, 3, 2, 1]))  # [2, 3, 4]
    print("result is ", task8( [-1, -2, -3, -4]))  # [-3, -2, -1]
    print("result is ", task8([]))  # 0
