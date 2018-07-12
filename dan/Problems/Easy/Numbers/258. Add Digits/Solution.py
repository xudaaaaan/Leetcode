import functools
class Solution:
    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = functools.reduce(lambda x, y: x + y, [int(i) for i in str(num)])
        return num
    
    
    def addDigits(self, num):
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9
            
