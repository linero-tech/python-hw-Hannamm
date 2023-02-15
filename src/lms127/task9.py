def task9(sentence, character):
    result = character.lower() in sentence.lower()
    return result


if __name__ == "__main__":
    print("result is", task9("I code in KOTLIN", "i"))
