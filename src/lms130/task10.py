
def task10(items):
    result = []

    for item in items:
        if item % 2 == 0:  # check if the item is even
            result.append(item * 2)  # multiply even items by 2
        else:
            result.append(item * 3)  # multiply odd items by 3

    return result


if __name__ == "__main__":
    print("result is ", task10([1, 2, 3, 4, 5]))  # [3, 4, 9, 8, 15]
    print("result is ", task10([9, 1, 2, 3, 6]))  # [27, 3, 4, 9, 12]
    print("result is ", task10([4]))  # [8]
    print("result is ", task10([1, -2, 3, -4]))  # [3, -4, 9, -8]
    print("result is ", task10([]))  # []
    print("result is ", task10([0, 1, 0, 1]))  # [0, 3, 0, 3]
    print("result is ", task10([1, 1, 1, 1]))  # [3, 3, 3, 3]
