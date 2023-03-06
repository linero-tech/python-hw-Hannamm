
def task7(items):
    result = 0

    if len(items) > 0:
        result = items[0]
    for item in items:
        if item < result:
            result = item

    return result


if __name__ == "__main__":
    print("result is ", task7([10, 5, 11]))  # 5
    print("result is ", task7([1, 2, 3, 4, 5]))  # 1
    print("result is ", task7([3, 2, 1, 4, 5]))  # 1
    print("result is ", task7([-100, -90, -10, 1, -2, 3]))  # -100
    print("result is ", task7([]))  # 0
