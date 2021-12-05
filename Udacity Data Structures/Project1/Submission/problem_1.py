class Node(object):
    def __init__(self, key, value, next=None, previous=None):
        self.key = key
        self.value = value
        self.previous = previous
        self.next = next


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.capacity = capacity
        self.no_elements = 0
        self.head = Node(None, None)
        self.tail = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            temp = self.head
            if self.cache[key].previous:
                self.cache[key].previous.next = self.cache[key].next
                if self.cache[key].next:
                    self.cache[key].next.previous = self.cache[key].previous
                else:
                    self.tail = self.cache[key].previous
                if self.cache[key].previous == self.head:
                    self.cache[key].previous.previous = self.cache[key]
                self.head = self.cache[key]
                self.head.previous = None
                self.head.next = temp
            return self.cache[key].value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.no_elements < self.capacity:
            if self.head.value == None:
                self.head = Node(key, value)
                self.cache[key] = self.head
                self.tail = self.head
            else:
                x = self.head
                self.head = Node(key, value)
                self.head.next = x
                self.head.next.previous = self.head
                self.cache[key] = self.head
            self.no_elements += 1
        else:
            ind = self.tail.key
            self.tail = self.tail.previous
            del self.cache[ind]
            x = self.head
            self.head = Node(key, value)
            self.head.next = x
            self.head.next.previous = self.head
            self.cache[key] = self.head


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))

our_cache = LRU_Cache(0)

our_cache.set(1, 1)  # ERROR because there's no available space


our_cache = LRU_Cache(-1)

our_cache.set(1, 1)  # ERROR because there's no available space
