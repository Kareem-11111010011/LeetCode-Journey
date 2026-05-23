class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        n = len(prices)
        dp = [0] * n
        minpsf = prices[0]

        for i in range(1, n):
            minpsf = min(minpsf, prices[i])
            dp[i] = max(dp[i-1], prices[i] - minpsf)

        return dp[-1]
