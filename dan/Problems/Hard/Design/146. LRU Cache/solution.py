class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val
        self.key = None
        
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.hash = {}
        self.last = Node(-1)
        self.first = Node(-1)
        self.last.next = self.first
        self.first.prev = self.last
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            node = self.hash[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not key in self.hash:
            node = Node(value)
            node.key = key
            self.hash[key] = node
            self.size += 1
            self._insert(node)
            if self.size > self.capacity:
                self.hash.pop(self.last.next.key)
                self._remove(self.last.next)
                self.size -= 1
                
        elif not value == self.hash[key].val:
            node = self.hash[key]
            node.val = value
            self._remove(node)
            self._insert(node)
      
            
    def _remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next = nxt
        nxt.prev = pre
        
    def _insert(self, node):
        orig = self.first.prev
        orig.next = node
        node.prev = orig
        node.next = self.first
        self.first.prev = node
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
