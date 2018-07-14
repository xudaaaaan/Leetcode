import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 0
        self.container = dict()
        self.helper = dict()
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.container.get(val, False):
            return False
        else:
            self.n += 1
            self.container[val] = self.n
            self.helper[self.n] = val
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.container.get(val, False):
            number = self.helper[self.n]
            index = self.container[val]
            self.container[number] = index
            self.helper[index] = number
            self.helper.pop(self.n)
            self.container.pop(val)
            self.n -= 1
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.n == 0:
            return False
        i = random.randint(1, self.n)
        return self.helper[i]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
