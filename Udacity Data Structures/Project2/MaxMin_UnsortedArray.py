import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_num = ints[0]
    max_num = ints[0]
    for x in ints:
        if x > max_num:
            max_num = x
        if x < min_num:
            min_num = x
    return min_num, max_num

# Example Test Case of Ten Integers


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

l2 = [i for i in range(5, 25)]  # a list containing 0 - 9
random.shuffle(l2)

l3 = [i for i in range(-8, 100)]  # a list containing 0 - 9
random.shuffle(l3)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((5, 24) == get_min_max(l2)) else "Fail")
print("Pass" if ((-8, 99) == get_min_max(l3)) else "Fail")
