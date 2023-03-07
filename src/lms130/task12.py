
def task12_1(sells):
    # max_sells = sells[0]
    # max_day = 0
    # for i in range(1, len(sells)):
    #     if sells[i] > max_sells:
    #         max_sells = sells[i]
    #         max_day = i
    # result1 = max_day
    max_sells = sells[0]
    max_day = "Monday"

    for i in range(1, len(sells)):
        if sells[i] > max_sells:
            max_sells = sells[i]
            max_day = ""

            if i == 1:
                max_day += "Tuesday"
            elif i == 2:
                max_day += "Wednesday"
            elif i == 3:
                max_day += "Thursday"
            elif i == 4:
                max_day += "Friday"
            elif i == 5:
                max_day += "Saturday"
            else:
                max_day += "Sunday"

    result = max_day

    return result


def task12_2(sells):
    # min_sells = sells[0]
    # min_day = 0
    # for i in range(1, len(sells)):
    #     if sells[i] < min_sells:
    #         min_sells = sells[i]
    #         min_day = i
    # result = min_day

    min_sells = sells[0]
    min_day = "Monday"

    for i in range(1, len(sells)):
        if sells[i] < min_sells:
            min_sells = sells[i]
            min_day = ""

            if i == 1:
                min_day += "Tuesday"
            elif i == 2:
                min_day += "Wednesday"
            elif i == 3:
                min_day += "Thursday"
            elif i == 4:
                min_day += "Friday"
            elif i == 5:
                min_day += "Saturday"
            else:
                min_day += "Sunday"

    result = min_day

    return result


def task12_3(sells):
    total_sells = 0
    for i in range(len(sells)):
        total_sells += sells[i]
    result = total_sells
    return result


if __name__ == "__main__":
    print("result is ", task12_1([20, 100, 800, 768, 765, 90, 10]))  # Wednesday
    print("result is ", task12_2([20, 100, 800, 768, 765, 90, 10]))  # Sunday]
    print("result is ", task12_3([20, 100, 800, 768, 765, 90, 10]))  # 2553
    print("result is ", task12_3([1, -2, 3, -4]))  # [3, -4, 9, -8]
    print("result is ", task12_3([]))  # []
    print("result is ", task12_3([0, 1, 0, 1]))  # [0, 3, 0, 3]
