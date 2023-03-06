def task3(items):
    result = []
    for i in items:
        if items.count(i) > 1 and i not in result:
            result.append(i)

    return result


if __name__ == "__main__":
    print("result is ", task3([]))  # []
    print("result is ", task3([1, 1, 1, 2, 2, 3]))  # [1,2]
    print("result is ", task3([0, 0, 0, 0]))  # [0]
    print("result is ", task3([-9, -9, 9, 1, 1, -9, 9, 3, 2, 2]))  # [-9, 9, 1, 2]
    print("result is ", task3([1, 1, -2, 3, 4]))  # [1]
    print("result is ", task3([5, 6, 5, 6, 7, 8, 7]))  # [5, 6, 7]
