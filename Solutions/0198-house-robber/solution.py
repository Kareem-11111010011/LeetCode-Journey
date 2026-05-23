class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0];
        if l == 2:
            return max(nums[0], nums[1])

        dp = [-1] * l
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]
        
        for i in range(3, l):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 3] + nums[i])
        
        return max(dp)
