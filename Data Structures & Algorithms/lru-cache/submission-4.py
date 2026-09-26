class ListNode:
    def __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.rcd = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev

    def _insert(self, node):
        first = self.head.nxt

        # node
        node.prev = self.head
        node.nxt = first

        # head and first
        self.head.nxt = node
        first.prev = node

    def get(self, key: int) -> int:
        if key in self.rcd:
            node = self.rcd[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.rcd:
            node = self.rcd[key]
            node.val = value
            self._remove(node)
            self._insert(node)
            return
        
        new_node = ListNode(key, value)
        self._insert(new_node)
        self.rcd[key] = new_node

        if len(self.rcd) > self.capacity:
            last = self.tail.prev
            self._remove(last)
            del self.rcd[last.key]

