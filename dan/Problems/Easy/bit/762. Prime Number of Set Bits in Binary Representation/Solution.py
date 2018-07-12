class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        primes = [2,3,5,7,11,13,17,19,23,29]
        for ele in range(L, R + 1):
            if bin(ele).count('1') in primes:
                res += 1
        return res
