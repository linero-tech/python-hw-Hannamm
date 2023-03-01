def task7(a, b):
    result = 1

    if a == 0 and b == 0:
        result = 1
    else:
        for i in range(b):
            result *= a

    return result


if __name__ == "__main__":
    print("result is ", task7(2, 3))
    # print("result is ", task7(4, 4))
    # print("result is ", task7(5, 3))
    # print("result is ", task7(2, 4))
