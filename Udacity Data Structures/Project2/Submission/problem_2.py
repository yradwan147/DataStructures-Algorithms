def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    if number < input_list[-1]:
        return binary_search(len(input_list)-input_list[-1], len(input_list)-1, input_list, number)
    else:
        return binary_search(0, len(input_list)-input_list[-1], input_list, number)


def binary_search(left, right, arr, target):
    mid = (right-left)//2
    space = arr[left:right]
    if space[mid] == target:
        return mid+left
    if len(space) == 1:
        return -1
    elif space[mid] > target:
        return binary_search(left, right-mid, arr, target)
    else:
        return binary_search(mid+left, right, arr, target)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Empty value
test_function([[], 10])
# Big value
test_function([[14, 15, 16, 17, 18, 19, 20, 21, 22, 1,
              2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 16])
