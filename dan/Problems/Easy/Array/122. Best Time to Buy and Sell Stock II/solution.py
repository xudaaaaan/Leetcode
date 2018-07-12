vclass Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) in [0, 1]:
            return 0
        return sum(prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] > prices[i - 1])
