class Solution(object):
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
        
    def isPalindrome(self, x):
        if x < 0:
            return False
        d, res = x, 0
        while not d == 0:
            rem = d % 10
            res = 10 * res + rem
            d = (d - rem) / 10
        return res == x
            
        
        
        
        
