class LRUCache:

    def __init__(self, capacity: int):
        self.back, self.front = QueueNode(), QueueNode()
        self.back.next, self.front.prev = self.front, self.back
        self.hashmap = {} # (value, pointer)
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_to_back(self.hashmap[key][1])
            return self.hashmap[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.move_to_back(self.hashmap[key][1])
            self.hashmap[key][0] = value
        else:
            if self.size < self.capacity:
                self.size += 1
            else:
                lru = self.front.prev.key
                before_lru = self.front.prev.prev
                self.front.prev, before_lru.next = before_lru, self.front
                self.hashmap.pop(lru)
            node = QueueNode(key, self.back, self.back.next)
            self.back.next.prev = node
            self.back.next = node
            self.hashmap[key] = [value, node]
        

    def move_to_back(self, pointer):
        if pointer is not self.back.next:
            before, after = pointer.prev, pointer.next
            last = self.back.next
            pointer.prev, pointer.next = self.back, last
            last.prev = pointer
            self.back.next = pointer
            before.next, after.prev = after, before


class QueueNode:
    def __init__(self, key=None, prev=None, next=None):
        self.prev, self.next = prev, next
        self.key = key
