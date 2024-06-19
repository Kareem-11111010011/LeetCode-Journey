class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = {nums[i]:0 for i in range(len(nums))}

        for i in range(len(nums)):
            if n[nums[i]] + 1 >= 2: return True
            n[nums[i]] += 1
        
        return False


