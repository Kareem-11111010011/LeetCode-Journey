class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zptr = 0
        for numptr in range(len(nums)):
            if nums[numptr] != 0:
                nums[zptr], nums[numptr] = nums[numptr], nums[zptr] 
                zptr += 1
        return nums 
            
        
