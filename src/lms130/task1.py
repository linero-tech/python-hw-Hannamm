def task1(items):
    import random

    if items:
        result = random.choice(items)
    else:
        result = 0

    return result


if __name__ == "__main__":
    print("result is ", task1([]))  # True
    print("result is ", task1([1, 2, 3, 4, 5, 6]))  # True
    print("result is ", task1([-1, -2, -3, -4, -5, -6]))
    print("result is ", task1([1, 2, 3, 4, 5]))
    print("result is ", task1([1, 2, 3, 4, 5]))
