def task6(sentence):
    result = ""

    for i in range(len(sentence)):
        if i % 2 == 0:
            result += sentence[i].upper()
        else:
            result += sentence[i]

    return result


if __name__ == "__main__":
    print("result is ", task6("I like Gothenburg"))  # I LiKe GOtHeNbUrG
    print("result is ", task6("I LOVE SWEDEN"))  # I LOVE SWEDEN
    print("result is ", task6("abcde"))  # AbCdE
    print("result is ", task6("abcdef abcde abcde"))  # AbCdEf aBcDe aBcDe
