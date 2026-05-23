class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        z = 0;
        o = 1;
        l = len(cost)
        dp = [-1] * l
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, l):
            if i + 1 == l:
                dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
                dp[i] = min(dp[i], dp[i - 1])
            else:    
                dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        
        return dp[-1]
