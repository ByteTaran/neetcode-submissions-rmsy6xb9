class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = prices[0]
        profit = sell - buy
        for price in prices:
            buy = min(price, buy)
            sell = max(price, buy)
            profit = max(profit, sell - buy)
        
        return profit