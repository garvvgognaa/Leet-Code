class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0

        min_cost = prices[0]
        max_profit = 0

        for i in range(n):
            profit = prices[i] - min_cost
            max_profit = max(max_profit, profit)
            min_cost = min(min_cost, prices[i])

        return max_profit
