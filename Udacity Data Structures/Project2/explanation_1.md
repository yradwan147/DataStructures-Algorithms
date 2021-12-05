### Problem 1: Square Root

The definiton of a square root of a number is that if this number is divided by its square root, it results in the same square root number. That's the point of the is_target function and I used binary search to search in the range of numbers under the inputted number since the square root must exist in this space.
This will require O(log(n)) time complexity due to binary search.

\*\* The range can be reduced to n/2 as well but it won't matter that much in time complexity.

### Problem 2: Search in Rotated Sorted Array

Assuming the list contains all numbers from 0 to n without the random pivot number, I can obtain the pivot index from the value of the last element in the list. After that I do binary search on one of the two halves depending on the value of the target number in comparison to the last element (number before the pivot).
This will require O(log(n)) time complexity due to binary search.

### Problem 3: Rearrange Array Digits For Maximum Sum of 2 Numbers

To obtain the largest sum, numbers should be sorted and then laid out one by one in each number step by step: biggest in the first number then the second biggest in the second number and so on. Since this requires O(nlog(n)) time complexity, I opted for mergesort since it's better in the case of large inputs while quicksort doesn't fair as well. Standard mergesort implementation then I loop through approximately log(n) as I build the 2 numbers from the list using powers of 10.
Time complexity: O(nlog(n)) as required.

### Problem 4: Dutch National Flag

The idea is to put 0 and 2 in their correct positions, which will make sure all the 1s are automatically placed in their right positions. This is a time complexity of O(n) since it involves a single traversal of the list as required in the problem.

### Problem 5: Autocomplete with Tries

This was pretty easy by following the instructions in the notebook. I used a generator to output the suffixes which I then iterated through using list() to get all suffixes. Time complexity is probably O(n) where n is the length of the longest suffix possible.

### Problem 6: Unsorted Integer Max/Min

This was pretty easily done by creating 2 variables and then updating one of them for the max value and the other for the minimum value during a single traversal of the list.
Time complexity: O(n)

### Problem 7: Request Routing

Similar time complexity and thought process to the autocomplete problem with the addition of using split to deal with pathes and strip to remove trailing slashes.
