class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        maxProfit =0

        for i,price in enumerate(prices):
            if price < buyPrice:
                buyPrice = price
            maxProfit = max(maxProfit, price-buyPrice)
        return maxProfit