class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums) + 1
        dp = [0] * n
        dp[0] = -float('inf')
        dp[1] = nums[0]

        for i in range(2, n):
            dp[i] = max(nums[i - 1], dp[i - 1] + nums[i - 1])
        
        return max(dp)
