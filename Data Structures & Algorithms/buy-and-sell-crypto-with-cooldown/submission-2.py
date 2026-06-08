class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                # Buy today or skip
                buy = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, True)
                dp[(i, buying)] = max(buy, cooldown)

            else:
                # Sell today (then cooldown for 1 day)
                sell = dfs(i + 2, True) + prices[i]
                
                # Hold the stock
                cooldown = dfs(i + 1, False)
                
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)