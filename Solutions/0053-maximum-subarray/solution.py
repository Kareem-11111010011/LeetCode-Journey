class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = -float('inf')
        curr = 0

        for num in nums:
            curr = max(num, curr + num)
            ms = max(ms, curr)
        return ms
