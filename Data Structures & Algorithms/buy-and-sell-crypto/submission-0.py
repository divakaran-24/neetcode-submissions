class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0,1
        max1 = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                newval = prices[r] - prices[l]                 
                if max1 < newval:
                    max1 = newval
            else:
                l = r
            r += 1
        return max1


        