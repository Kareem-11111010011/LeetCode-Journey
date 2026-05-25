class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = set()
        ret = 0
        l = 0

        for r in range(len(s)):
            if s[r] in longest:
                while s[r] in longest:
                    longest.remove(s[l])
                    l += 1

            longest.add(s[r])
            ret = max(ret, r - l + 1)

        return ret
