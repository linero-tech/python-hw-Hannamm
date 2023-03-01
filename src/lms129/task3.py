def task3(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("result  is ", task3(5))
    print("result  is ", task3(4))  # 24
    print("result  is ", task3(6))  # 4720
