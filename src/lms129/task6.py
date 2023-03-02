
def task6(number):
    result = 0
    while number > 0:
        digit = number % 10  # Get the last digit of the number
        result = result * 10 + digit  # Add the digit to the result in reverse order
        number //= 10  # Remove the last digit from the number

    return result


if __name__ == "__main__":
    print("result is ", task6(678))
    print("result is ", task6(1))
    # print("result is ", task6(11))
    # print("result is ", task6(5))
    # print("result is ", task6(21))
    # print("result is ", task6(1234))
    # print("result is ", task6(23))

