class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        i = 0
        res = 0
        for height in sorted(heights):
            if height == heights[i]:
                i += 1
                continue
            else:
                res += 1
                i += 1
        return res
