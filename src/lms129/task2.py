def task2(number):
    result = True
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                result = False
                break

    return result


# A prime number is as a positive integer >=1
# with only two factors: itself and one
if __name__ == "__main__":
    print("result  is ", task2(5))  # True
    print("result  is ", task2(3))  # True
    print("result  is ", task2(7))  # True
    print("result  is ", task2(4))  # False
    print("result  is ", task2(26))  # False
