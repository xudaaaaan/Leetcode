class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        dp = [1 for _ in range(len(s))]
        for i in range(1, len(s)):
            t = int(s[i-1] + s[i])
            if s[i] == "0":
                if s[i - 1] in ["1","2"]:
                    dp[i] = dp[i - 2] if i > 1 else 1
                else:
                    dp[i] = 0
            else:
                dp[i] = dp[i - 1]
                if 10 < t <= 26:
                    dp[i] = (dp[i] + dp[i - 2]) if i > 1 else (dp[i] + 1)
        return dp[len(s) - 1]
        
        
