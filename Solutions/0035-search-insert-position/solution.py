class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            middle = left + ((right - left) // 2)
            if nums[middle] >= target:
                right = middle
            else:
                left = middle + 1
        return left
            
