class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minSoFar = float('inf')

        for price in prices:
            minSoFar = min(minSoFar, price)

            maxProfit = max(maxProfit, price - minSoFar)
        
        return maxProfit
            
