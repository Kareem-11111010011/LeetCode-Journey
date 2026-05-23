class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {num:0 for num in nums}
        out = []

        for num in nums:
            d[num] += 1
        
        for i in range(k):
            msf = max(d, key=d.get)
            out.append(msf)
            d.pop(msf)
        return out
