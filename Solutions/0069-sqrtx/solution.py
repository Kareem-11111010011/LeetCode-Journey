class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        l = 1
        r = x
        s = 0
        while l <= r:
            m = l + (r - l) // 2
            s = m * m
            if x > s:
                l = m + 1
            elif x < s:
                r = m - 1
            else:
                return m

        return l - 1
