### Problem 1 LRU Cache

To maintain constant time in my functions, I used a map/dictionary to allow constant time getter/setter functions, in addition to a doubly linked list to keep track of what element is the least recently used so that I can remove that element from the cache in constant time as well since I only need to check the tail of the list and remove it from the cache using the stored key in the tail node.

> The get() function is in constant time since the size of the cache is always less than or equal to 5. O(5) or O(<5) are all in constant time. All alterations to the doubly linked list are also basically in constant time O(1): They are done to move elements to the top of the "used" history when they are called by the user.
> The set() function is in constant time as well. If there's space in the cache then insertion in a linked list and in a dictionary are in constant time O(1). If the cache is full then a removal and an insertion are both required. Removal is in constant time since we can retrieve the key for the least recently used element from the tail of the linked list (constant time) and then remove it from the cache and the linked list which are also both in constant time (removing last element of linked list is constant time). Then insertion is again in constant time like in the previous case.

### Problem 2 File Recursion

This problem requires recursion and so I created my code according to the following steps:

1. Check all items in my given directory path (using os.listdir()) and then separate them into files and folders using os.path.isfile()
2. My break case for my recursion is if there are no directories left in my current working directory so I add that in line 28
3. Next, I first check through files in my current directory if they satisfy my suffix condition and if so I add them to my final output.
4. Finally, I do my recursive call of my function on all directories inside my working directory, extending my output with each call and then returning the full output in the end.

> Concerning time complexity for each step (where n = number of files in directory):

1. O(n) for os.listdir() and also for the separation loops for file_list and dir_list which, in the worst case scenario, each of them will take O(n/2).
2. N/A
3. If all files in directory are files (not folders) then, O(n)
4. In the worst case scenario, all files in the first path are folders/directories, in which case the recursive loop will run an O(n) time complexity.

### Problem 3 Huffman Coding

By following the steps in the instructions, I first created a frequency dictionary for the inputted string and then I inserted all elements of the dictionary as nodes into a minheap. After that, I "condensed" the minheap into a single huffman tree present at the first element of the minheap. Next, I generated the encoding for each letter using the tree by using the ".char" attribute of nodes as my guide and "0" to represent left movements and "1" to represent right movements, thus generating the huffman encoding.

The decoding is simply executing the movements in the encoding in the tree and adding a character to the result whenever we reach a leaf node and then resetting to the root node.

> Concerning time complexity for each step (n = number of letters in string:

# Encoding

1. O(n) for generating the frequency dictionary
2. O(log(n)) for inserting each element into the minheap
3. O(log(n)) for condensing the minheap
4. O(log(n)) for finding the path(encoding) of each letter

# Decoding

1. O(log(n)) for traversing the tree for each letter in the encoding

### Problem 4 Active Directory

To construct a recursive solution to this problem, I knew that if the user was found at least once in the main group or its subgroups then the answer will be true. Based on that, I wrote my base function to search inside the users of the inputted group for the targeted user and return 1 if he/she exists or 0 if he does not. Then I make my recursive function call on all the inputted groups' subgroups and sum up all the outputs. Thus, if the output equals anything more than 0, then the user exists. Else, he/she doesn't exist.

> Concerning time complexity: The "if user in group.users" runs in linear time complexity O(n) on the users list and the recursive call for loop also runs in O(n) but on the length of the groups list.

### Problem 5 Blockchain

To construct a linked list using "Blocks", I simply created my Block class using the given attributes and then created my Blockchain class which requires the instantiation of a tail element which also equates to its head since its length at first is 1. In this case I'm making a back-linked list so the head isn't important to me so I didn't keep track of it.

For each block instantiation, I calculated its hash using the given hash function (inputting its data, timestamp and previous hash since the hash should express the entire block from what I understood from the question).

When inserting elements into the blockchain, their attributes are inserted into a new block and the previous hash is set to the tail block hash. The tail is then set to the new block.

I calculated all timestamps using the GMT conversion of time.time() from the time library since I didn't know if I should calculate this or it will be given with each block from the user.

> The insert function and calc_hash function are both in constant time from what I understand as long as the hashlib library functions are in constant time but from what I read online, they might be closer to linear time complexity O(n).

### Problem 6 Union & Intersection

For this problem I based my solution off of basic probability formulas where A U B is A + B - A (intersection) B.
To calculate the intersection I need to find the contents of one of the linked lists and then run through the other comparing each element as I go since I can't compare elements of both lists concurrently. Going through the entirety of linked list 1 is linear time complexity O(n1) and then iterating through each element in the second is O(n2) but the "in" statement inside the for loop is also O(n1) so the comparison for loop is O(n2\*n1). Through this I obtain the intersection.

For the union I have to get the entire contents of both linked lists first and then add them together and remove the intersection. Looping through each list is O(n) respectively and then adding them together is constant time and then I have to run the intersection function again which is basically O(n^2) and then loop through the intersection and remove it from the union list which is O(n) as well in the worst case scenario when the two lists are identical.

> So, in short, both functions are O(n^2). I couldn't think of a way to make it better.
