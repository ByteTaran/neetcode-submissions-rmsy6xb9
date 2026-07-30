class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = temp = prices[0]

        profits = 0
        profit = 0
        for price in prices:
            buy = min(buy, price)
            sell = max(buy, price)
            if profit > sell - buy:
                profits += profit
                buy = price
            profit = sell - buy
        
        profits += profit

        return profits


