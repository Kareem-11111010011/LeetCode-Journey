class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = {}
        ret = count = 0
        l = 0
        r = len(s) - 1

        while l <= r:
            if not s[r] in longest and not s[l] in longest:
                longest[s[l]] = l
                l += 1
                count += 1
            elif s[r] in longest:
                r -= 1
            else:
                l = longest[s[l]] + 1
                ret = max(ret, count)
                r = len(s) - 1
                count = 0
                longest = {}
        
        return max(ret, count)
