### Problem 1: Square Root

The definiton of a square root of a number is that if this number is divided by its square root, it results in the same square root number. That's the point of the is_target function and I used binary search to search in the range of numbers under the inputted number since the square root must exist in this space.
This will require O(log(n)) time complexity due to binary search.

\*\* The range can be reduced to n/2 as well but it won't matter that much in time complexity.
Space complexity is O(1)

### Problem 2: Search in Rotated Sorted Array

Assuming the list contains all numbers from 0 to n without the random pivot number, I can obtain the pivot index from the value of the last element in the list. After that I do binary search on one of the two halves depending on the value of the target number in comparison to the last element (number before the pivot).
This will require O(log(n)) time complexity due to binary search.

Space complexity is O(1)

### Problem 3: Rearrange Array Digits For Maximum Sum of 2 Numbers

To obtain the largest sum, numbers should be sorted and then laid out one by one in each number step by step: biggest in the first number then the second biggest in the second number and so on. Since this requires O(nlog(n)) time complexity, I opted for mergesort since it's better in the case of large inputs while quicksort doesn't fair as well. Standard mergesort implementation then I loop through approximately log(n) as I build the 2 numbers from the list using powers of 10.
Time complexity: O(nlog(n)) as required.

Space complexity is O(n) due to merge sort, the loops to build the numbers have a space complexity of O(2) which is constant time so the overall complexity is O(n)

### Problem 4: Dutch National Flag

The idea is to put 0 and 2 in their correct positions, which will make sure all the 1s are automatically placed in their right positions. This is a time complexity of O(n) since it involves a single traversal of the list as required in the problem.

Space complexity is O(1)

### Problem 5: Autocomplete with Tries

This was pretty easy by following the instructions in the notebook. I used a generator to output the suffixes which I then iterated through using list() to get all suffixes.

> Time/Space complexity:

- TrieNode initialization -->
  Time Complexity: O(1), Space Complexity: O(1)
- TrieNode.insert -->
  Time Complexity: O(1), Space Complexity: O(x) (x in this case is 1 which is the size of one character to be inserted)
- TrieNode.suffixes -->
  Time complexity(worst case): O(nk) where n is the number of nodes and k is the size of the alphabet, Space complexity: O(1)

- Trie initialization -->
  Time Complexity: O(1), Space Complexity: O(1)
- Trie.insert -->
  Time complexity: O(n), Space complexity: O(n)
- Trie.find -->
  Time complexity: O(n), Space complexity: O(1)

### Problem 6: Unsorted Integer Max/Min

This was pretty easily done by creating 2 variables and then updating one of them for the max value and the other for the minimum value during a single traversal of the list.
Time complexity: O(n)

Space complexity is O(1)

### Problem 7: Request Routing

Similar time complexity and thought process to the autocomplete problem with the addition of using split to deal with pathes and strip to remove trailing slashes.

> Time/Space complexity:
> (n = number of segments of path)

- RouteTrieNode initialization -->
  Time Complexity: O(1), Space Complexity: O(1)
- RouteTrieNode.insert -->
  Time Complexity: O(1), Space Complexity: O(1) (because n=1)

- RouteTrie initialization -->
  Time Complexity: O(1), Space Complexity: O(1)
- RouteTrie.insert -->
  Time complexity: O(n), Space complexity: O(n)
- RouteTrie.find -->
  Time complexity: O(n), Space complexity: O(1)

- Router initialization -->
  Time Complexity: O(1), Space Complexity: O(1)
- Router.add_handler -->
  == RouteTrie.insert= Time: O(n), Space: O(n)
- Router.lookup -->
  == RouterTrie.find = Time: O(n), Space: O(1)
