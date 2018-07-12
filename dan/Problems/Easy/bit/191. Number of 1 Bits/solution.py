class Solution(object):
    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(map(int, bin(n)[2:]))
    
    def hammingWeight(self, n):
        cnt = 0
        while n > 0:
            if n & 1 == 1:
                cnt += 1
            n >>= 1
        return cnt
    
    
