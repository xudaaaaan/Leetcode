class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pmin, profit = 0, 0
        for i in range(1, len(prices)):
            if prices[pmin] > prices[i]:
                pmin = i
            profit = max(profit, prices[i] - prices[pmin])
        return profit
