class Solution:
    def minCostClimbingStairs1(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]
    
    def minCostClimbingStairs(self, cost):
        a, b = 0, 0
        for i in range(len(cost) - 1):
            a, b = b, min(a + cost[i], b + cost[i + 1])
        return b


