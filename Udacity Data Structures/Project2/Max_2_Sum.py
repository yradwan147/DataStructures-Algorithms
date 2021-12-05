import math


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = mergesort(input_list, len(input_list))
    num1 = 0
    num2 = 0
    x = 0
    for i in range(math.ceil(len(input_list)/2)):
        power = math.ceil(len(input_list)/2)-1
        num1 += sorted_list[-1-x]*(10**(power-i))
        try:
            num2 += sorted_list[-2-x]*(10**(power-i))
        except:
            num2 = num2//10
        x += 2
    print(x)
    return num1, num2


def mergesort(items, length):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left, length)
    right = mergesort(right, length)

    return merge(left, right)


def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 6, 2, 5], [64, 52]])
test_function([[4, 6, 5], [64, 5]])
