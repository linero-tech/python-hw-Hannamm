
def task11_1(guests):
    return len(guests)


def task11_2(guests, condition):
    return [guest for guest in guests if guest.endswith(condition)]


if __name__ == "__main__":
    # Change the situation to either "-V", "-A", or "-K" to test your code under different situation
    situation = "-K", "A"
    guest_list = [
        "Stéphanie-A",
        "Edmée-K",
        "Maëlla-K",
        "Océanne-K",
        "Géraldine-K",
        "Maëline-K",
    ]

    print(f"The event has a total of {task11_1(guest_list)} guests.")
    print(f"The attendees with condition '{situation}' are {task11_2(guest_list, situation)}")
