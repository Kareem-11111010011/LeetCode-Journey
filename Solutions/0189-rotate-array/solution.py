class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            return
        for i in range(1, k + 1):
            nums.insert(0, nums[-i])
        del nums[-k:]    
        
