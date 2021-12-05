def is_target(number, solution):
    if number // solution == solution:
        return 0
    else:
        if number // solution > solution:
            return 1
        elif number // solution < solution:
            return -1


def binary_search(left, right, number, arr):
    mid = (right - left)//2
    space = arr[left:right]
    if is_target(number, space[mid]) == -1:
        return binary_search(left, right-mid, number, arr)
    elif is_target(number, space[mid]) == 1:
        return binary_search(mid+left, right, number, arr)
    else:
        return space[mid]


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 1:
        return 1
    if number == 0:
        return 0
    arr = list(range(number))
    return binary_search(0, len(arr), number, arr)


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
