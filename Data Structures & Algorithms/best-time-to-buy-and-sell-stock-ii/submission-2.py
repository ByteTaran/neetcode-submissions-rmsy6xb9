class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if prevPrice < price:
                maxProfit += (price - prevPrice)
            prevPrice = price
        
        return maxProfit