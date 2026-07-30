class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = prices[0]
        maxProfit = 0

        for price in prices:
            buy = min(buy, price)
            sell = max(buy, price)
            maxProfit = max(maxProfit, sell - buy)

        return maxProfit