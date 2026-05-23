class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vals = {}
        for num in nums:
            vals[num] = vals.get(num, 0) + 1
        return max(vals, key=vals.get)
