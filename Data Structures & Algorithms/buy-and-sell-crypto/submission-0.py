class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0 #tracking variables
        current_min = prices[0]

        #go through prices and calculate profits using min
        for price in prices:
            if price < current_min:
                current_min = price
                continue
            if price - current_min > max_profit:
                max_profit = price - current_min
        return max_profit
            