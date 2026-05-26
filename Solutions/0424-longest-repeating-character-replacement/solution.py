class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        ret = 0

        l = 0
        mostFreq = 0
        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            mostFreq = max(mostFreq, freqMap[s[r]])

            swaps = (r - l + 1) - mostFreq
            if swaps <= k:
                ret = max(ret, r - l + 1)
            else:
                freqMap[s[l]] -= 1
                l += 1
        
        return ret
