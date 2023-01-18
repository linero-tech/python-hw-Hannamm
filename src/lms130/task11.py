from to_do import TODO


def task11_1(guests):
    return TODO(
        "Replace this 'TODO' with the variable 'result'. Do not erase the 'return' keyword"
    )


def task11_2(guests, condition):
    return TODO(
        "Replace this 'TODO' with the variable 'result'. Do not erase the 'return' keyword"
    )


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

    # NOTE: Uncomment the code below when you are ready to test your answers
    print(f"The event has a total of {task11_1(guest_list)} guests.")
    print(
        f"The attendees with condition '{situation}' are {task11_2(guest_list, situation)}"
    )
