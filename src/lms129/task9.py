
def task9(temperature):
    result = 0
    if temperature[-1].upper() == "C":
        degree = int(temperature[:-1])
        result = round(degree * 9 / 5 + 32)
        result = str(result) + "F"
    elif temperature[-1].upper() == "F":
        degree = int(temperature[:-1])
        result = round((degree - 32) * 5 / 9)
        result = str(result) + "C"
    return result


if __name__ == "__main__":
    print("result is ", task9("-30C"))
    print("result is ", task9("50F"))
    # print("result is ", task9("40c"))
    # print("result is ", task9("-65f"))
