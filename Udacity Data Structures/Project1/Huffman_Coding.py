import sys


class Node(object):
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __repr__(self):
        return ('##' + str(self.char) + ":" + str(self.freq) + '##')
        #+ "||" + str(self.left) + "||" + str(self.right)


class MinHeap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        # print("inside heapify")
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            # print("Parent: " + str(parent_element.freq) +
            #       " Child: " + str(child_element.freq))
            # l = input('')
            if parent_element.freq > child_element.freq:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                child_index -= 1

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                if parent.freq > left_child.freq:
                    min_element = left_child
                else:
                    min_element = parent

            # compare with right child
            if right_child is not None:
                if parent.freq > right_child.freq:
                    if right_child.freq > left_child.freq:
                        min_element = left_child
                    else:
                        min_element = right_child
                elif parent.freq > left_child.freq:
                    min_element = left_child
                else:
                    min_element = parent

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

    def condense(self):
        if self.size() == 1:
            return None
        first = self.remove()
        second = self.remove()
        if first.freq > second.freq:
            left = second
            right = first
        else:
            left = first
            right = second
        new_node = Node(left.char+right.char, first.freq +
                        second.freq, left, right)
        self.insert(new_node)

    def path_to_encoding(self, root, letter):
        res = ''
        node = root
        while node.char != letter:
            if letter in node.left.char:
                node = node.left
                res += '0'
            elif letter in node.right.char:
                node = node.right
                res += '1'

        return res

    def encode(self, string):
        if self.size() != 1:
            return None
        res = ''
        for letter in string:
            res += self.path_to_encoding(self.cbt[0], letter)
        return res


def huffman_encoding(data):
    minheap = MinHeap()
    freq_dict = {}
    for letter in data:
        freq_dict[letter] = freq_dict.get(letter, 0)+1
    # p = input('')
    for key, value in freq_dict.items():
        minheap.insert(Node(key, value))
    while minheap.size() > 1:
        minheap.condense()
    return minheap.encode(data), minheap


def huffman_decoding(data, tree):
    node = tree.cbt[0]
    res = ''
    for bit in data:
        if bit == '0':
            if node.left:
                node = node.left
                # print('left')
            else:
                # print('reset_left')
                res += node.char
                node = tree.cbt[0].left
        elif bit == '1':
            if node.right:
                node = node.right
                # print('right')
            else:
                # print('reset_right')
                res += node.char
                node = tree.cbt[0].right
    res += node.char
    return res


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = "alo"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = " l "

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = "llaaooqqbbwwkkssiixxhhaallwewuurrnneebbvvmmzznnuuddoojjuuhhggssppqqoowiiee"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print(encoded_data)
    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
