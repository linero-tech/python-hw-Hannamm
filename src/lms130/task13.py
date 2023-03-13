def task13_1(customers):
    return list(set(customers))


def task13_2(customers):
    from collections import Counter

    return [email for email, count in Counter(customers).items() if count > 1]


def task13_3(customers):
    return list(set([email.split('@')[1] for email in customers]))


if __name__ == "__main__":
    customer_list = [
        "mary@tv.com",
        "john@nas.gov",
        "john@nas.gov",
        "ema@post.com",
        "ema@post.com"
    ]

    print(f"The customers who purchased from your product: {task13_1(customer_list)}")
    print(
        f"The customers that purchased multiple times include: {task13_2(customer_list)}"
    )
    print(f"The companies that purchased from you include: {task13_3(customer_list)}")
