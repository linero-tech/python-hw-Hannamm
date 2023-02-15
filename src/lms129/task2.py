
def task2(number):

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                result = False
                break
        else:
         result = True
    else:
        result = False
    return result


if __name__ == "__main__":
    print("result  is ", task2(5))
