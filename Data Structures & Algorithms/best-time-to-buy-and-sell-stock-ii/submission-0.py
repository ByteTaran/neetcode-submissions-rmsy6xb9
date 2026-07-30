class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = temp = prices[0]

        profits = list()
        profit = 0
        for price in prices:
            buy = min(buy, price)
            sell = max(buy, price)
            if profit > sell - buy:
                profits.append(profit)
                buy = price
            profit = sell - buy
        
        profits.append(profit)

        return sum(profits)


