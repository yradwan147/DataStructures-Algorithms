class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def intersection(llist_1, llist_2):
    # Your Solution Here
    intersect = []
    llist1_content = []
    node = llist_1.head
    while node:
        llist1_content.append(node.value)
        node = node.next
    node = llist_2.head
    while node:
        if node.value in llist1_content:
            intersect.append(node.value)
        node = node.next
    return intersect


def union(llist_1, llist_2):
    llist1_content = []
    llist2_content = []
    node = llist_1.head
    while node:
        llist1_content.append(node.value)
        node = node.next

    node = llist_2.head
    while node:
        llist2_content.append(node.value)
        node = node.next

    #print(llist1_content, llist2_content)
    union = llist1_content + llist2_content
    intersect = intersection(llist_1, llist_2)
    #print(union, intersect)
    for x in intersect:
        union.remove(x)
    return union


# Test case 1


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# [3, 2, 35, 65, 4, 3, 6, 32, 4, 9, 6, 1, 11, 21, 1]
print(union(linked_list_1, linked_list_2))
# [6, 4, 6, 21]
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

# [3, 2, 4, 35, 6, 65, 6, 4, 3, 23, 1, 7, 8, 9, 11, 21, 1]
print(union(linked_list_3, linked_list_4))
# []
print(intersection(linked_list_3, linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

# [3, 2, 4, 35, 6, 65, 6, 4, 3, 23, 1, 7, 8, 9, 11, 21, 1]
print(union(linked_list_3, linked_list_4))
# []
print(intersection(linked_list_3, linked_list_4))
