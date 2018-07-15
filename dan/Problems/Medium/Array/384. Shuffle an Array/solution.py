import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.list = nums
        self.dic = {}
        self.k = len(nums)
        for i, n in enumerate(self.list):
            self.dic[i] = n

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        for i in range(self.k):
            self.list[i] = self.dic[i]
        return self.list
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        index = list(range(self.k))
        random.shuffle(index)
        for i, j in enumerate(index):
            self.list[i] = self.dic[j]
        return self.list
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
