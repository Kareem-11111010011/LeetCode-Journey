class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nd = {}
        for i, num in enumerate(nums):
            if target - num in nd:
                return [nd[target - num], i]
            nd[num] = i
