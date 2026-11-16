from collections import defaultdict

class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.tail = None  # will store LRU
        self.head = None  # stores most recent

    def get(self, key: int) -> int:
        if key in self.cache:
            if self.cache[key] == self.head:
                pass
            elif self.cache[key] == self.tail:
                # update the linkedlist
                prev = self.cache[key].prev
                self.tail = prev

                # move it to the head
                self.cache[key].next = self.head
                self.cache[key].prev = None
                self.head.prev = self.cache[key]
                self.head = self.cache[key]

                # rejoin severed
                prev.next = None
            else:
                # update the linkedlist
                nextt = self.cache[key].next
                prev = self.cache[key].prev
                
                # move it to head
                self.cache[key].next = self.head
                self.cache[key].prev = None
                self.head.prev = self.cache[key]
                self.head = self.cache[key]

                # rejoin severed linkedlist
                prev.next = nextt
                nextt.prev = prev

            return self.cache[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            new_node = Node(value, key)
            self.cache[key] = new_node
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else: # add first one
                self.head = new_node
                self.tail = new_node
        else:
            self.cache[key].val = value

        if len(self.cache.items()) > self.capacity:
            # get rid of tail from cache and from the linkedlist

            self.cache.pop(self.tail.key)

            new_tail = self.tail.prev
            self.tail.prev.next = None
            self.tail = new_tail
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)