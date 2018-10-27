class Solution(object):
    #TLE
    def change1(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins = sorted(coins, reverse = True)
        stack = [(amount, -1)]
        res = 0
        while stack:
            residual, last_coin = stack.pop()
            if residual == 0:
                res += 1
            elif last_coin < len(coins) - 1:
                cur = coins[last_coin + 1]
                i = 0
                while residual - cur * i >= 0:
                    stack.append((residual - cur * i, last_coin + 1))
                    i += 1
        return res
    #dp
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[amount]
        
        


