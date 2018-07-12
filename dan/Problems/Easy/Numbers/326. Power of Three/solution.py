import math
class Solution:
    def isPowerOfThree1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        a = math.log(n)
        b = math.log(3)
        return abs(a / b - int(a / b)) < 0.00000000001 or abs(a / b - int(a / b) - 1) < 0.00000000001
    
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0
