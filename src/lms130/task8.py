def task8(items):
    # remove duplicates from the items list
    unique_items = list(set(items))

    # if the length of the unique items is less than or equal to 3, return them
    if len(unique_items) <= 3:
        result = sorted(unique_items)
    else:
        # sort the unique items in descending order
        unique_items_sorted = sorted(unique_items, reverse=True)
        # take the first three items from the sorted list
        result = unique_items_sorted[:3]
        # sort the result list in ascending order
        result = sorted(result)

    return result


if __name__ == "__main__":
    print("result is ", task8([60, 9, 7, 10]))  # [9, 10, 60]
    print("result is ", task8([1, 2, 3, 4, 5]))  # [3, 4, 5]
    print("result is ", task8([4, 3, 2, 1]))  # [2, 3, 4]
    print("result is ", task8([-1, -2, -3, -4]))  # [-3, -2, -1]
    print("result is ", task8([]))  #
    print("result is ", task8([-1, -1, -1, -1]))  # -1
