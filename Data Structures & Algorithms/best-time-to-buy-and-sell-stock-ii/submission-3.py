class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = sell = prices[0]
        for price in prices:
            if price < sell:
                profit += sell - buy
                buy = sell = price
            elif price > sell:
                sell = price

        profit += sell - buy
        return profit