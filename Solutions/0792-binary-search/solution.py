class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        middle = len(nums) // 2
        while True:
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                middle += 1
            else:
                middle -= 1
            
