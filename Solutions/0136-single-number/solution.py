class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index = 0
        nums = sorted(nums)
        while True:
            if len(nums) == 1:
                return nums[index]
            elif nums[index] == nums[index + 1]:
                nums.pop(index)
                nums.pop(index)
            else:
                return nums[index]
                
