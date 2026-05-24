class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ret = nums[0]
        count = 0
        for num in nums:
            if num != ret:
                count -= 1
                if count < 0:
                    ret = num
                    count = 0
            else:
                count += 1

        return ret
