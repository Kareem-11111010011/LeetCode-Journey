class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = [-1] * len(nums)

        i = 0
        j = len(nums) - 1
        e = j

        while e >= 0:
            if abs(nums[i]) >= abs(nums[j]):
                ret[e] = nums[i] ** 2
                i += 1
            else:
                ret[e] = nums[j] ** 2
                j -= 1
            e -= 1
        
        return ret
