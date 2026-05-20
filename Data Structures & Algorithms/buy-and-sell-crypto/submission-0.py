class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            if i > 0:
                current_profit = prices[i] - min_price
                profit = max(profit, current_profit)
        return profit
        