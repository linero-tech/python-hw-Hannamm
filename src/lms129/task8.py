def task8(number):
    result = 0
    for digit in str(number):
        result += int(digit)
    return result


if __name__ == "__main__":
    print("result is ", task8(123))  # 6
    # print("result is ", task8(365))  # 14
    # print("result is ", task8(978))  # 24
    # print("result is ", task8(371))  # 11
