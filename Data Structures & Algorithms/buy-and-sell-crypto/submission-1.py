class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        max_prices = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                new_prices = prices[r] - prices[l]
                if max_prices < new_prices:
                    max_prices = new_prices
            else:
                l = r
            r += 1
        return max_prices
 