from to_do import TODO

def task5(value_for_a, value_for_b):
    a = value_for_a
    b = value_for_b

    temp = a
    a = b
    b = temp

        # Do not erase or change the below statement
    return a, b
if __name__ == "__main__":
    print(f"a is {task5(1,2)[0]} \nb is {task5(1,2)[1]}" )

