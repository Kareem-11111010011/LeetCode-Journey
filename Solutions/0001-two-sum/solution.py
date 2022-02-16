class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 1
        while nums[j] != target - nums[i]:
            j += 1
            if j == len(nums):
                j = i + 2
                i += 1
        return [i, j]
