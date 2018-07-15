class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1 for i in range(amount)]
        for money in range(1, amount + 1):
            n, flag = float('inf'), False
            for coin in coins:
                if money - coin >= 0 and not dp[money - coin] == -1:
                    n = min(dp[money - coin] + 1, n)
                    flag = True
            if flag:
                dp[money] = n
        return dp[-1]
     
