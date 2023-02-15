
def task1(a, b):
    result = 0
    if a < b:
        result = sum(range(a, b+1))
        return result


if __name__ == "__main__":
    print("result is", task1(1, 5))

def task_2(a, b):
    result = 0
    if a < b:
        for i in range(a, b+1):
            result += i
        else:
            result = 0
    return result


if __name__ == "__main__":
    print("result is", task_2(3, 3))
