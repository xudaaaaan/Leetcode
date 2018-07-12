import collections

class MyStack1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        ls = []
        while not self.empty():
            ls.append(self.queue.popleft())
        for i in range(len(ls) - 1):
            self.queue.append(ls[i])
        return ls[-1]
        
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        ls = []
        while not self.empty():
            ls.append(self.queue.popleft())
        for i in range(len(ls)):
            self.queue.append(ls[i])
        return ls[-1]
                

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if self.queue else True
    

import collections

class MyStack:

    def __init__(self):
        self.queue = collections.deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q = self.queue
        q.append(x)
        for i in range(len(q) - 1):
            q.append(q.popleft())
        
    def pop(self):
        return self.queue.popleft()
        
    def top(self):
        return self.queue[0]
                

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if self.queue else True
    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
