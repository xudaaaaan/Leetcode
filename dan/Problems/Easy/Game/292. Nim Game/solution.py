class Solution:
    # Time exceed error!
    def canWinNim1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in [1, 2, 3]:
            return True
        dp = [False for _ in range(n + 1)]
        dp[1:4] = [True for _ in range(3)] 
        
        for i in range(4, n + 1):
            for j in [1, 2, 3]:
                if not dp[i - j]:
                    dp[i] = True
                    break
        return dp[n]
    
    def canWinNim(self, n):
        return not n % 4 == 0

        
