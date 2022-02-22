class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in range(0, len(nums)):
            if num in nums:
                continue
            return num
        return len(nums)
