
def task9(temperature):
    # if temperature[-1] == "C" or temperature[-1] == "c":
    #     # Convert from Celsius to Fahrenheit
    #     result = float(temperature[:1]) * 9 / 5 + 32
    #     result = str(result) + "F"
    # elif temperature[-1] == "F" or temperature[-1] == "f":
    #     # Convert from Fahrenheit to Celsius
    #     result = (float(temperature[:1]) - 32) * 5 / 9
    #     result = str(result) + "C"
    # else:
    #     result = "Invalid input"
    import math

    if temperature[-1] == "C" or temperature[-1] == "c":
        # Convert from Celsius to Fahrenheit
        result = float(temperature[:-1]) * 9 / 5 + 32
        result = str(math.trunc(result)) + "F"
    elif temperature[-1] == "F" or temperature[-1] == "f":
        # Convert from Fahrenheit to Celsius
        result = (float(temperature[:-1]) - 32) * 5 / 9
        result = str(math.trunc(result)) + "C"
    else:
        result = "Invalid input."

    return result


if __name__ == "__main__":
    print("result is ", task9("-30C"))  # -22F
    print("result is ", task9("50f"))  # 10C
    print("result is ", task9("1C"))  # 33F
    print("result is ", task9("0F"))  # 17C
    print("result is ", task9("-90F"))  # -67
    print("result is ", task9("20f"))  # -6C
    print("result is ", task9("1"))  # invalid
    print("result is ", task9("0h"))  # invalid
