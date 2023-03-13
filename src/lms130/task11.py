from to_do import TODO


def task11_1(guests):
    result = len(guests)

    return result


def task11_2(guests, condition):
    condition = "-K"
    return [guest for guest in guests if guest.endswith(condition)]


if __name__ == "__main__":
    # Change the situation to either "-V", "-A", or "-K" to test your code under different situation
    situation = "-V"
    guest_list = [
        "Stéphanie-A",
        "Edmée-K",
        "Maëlla-K",
        "Océanne-K",
        "Géraldine-K",
        "Maëline-K",
    ]

    print("result is", task11_1(["Lia-K", "Mar-A", "Luz-K", "Ulf-V"]))
    print("result is", task11_2(["Lia-K", "Mar-A", "Luz-K", "Ulf-V"], "-V"))
