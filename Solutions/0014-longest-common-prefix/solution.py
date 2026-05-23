class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        si = 0

        if len(strs) == 1:
            return strs[0]

        for string in strs:
            if string == "":
                return ""

        while True:
            for i in range(1, len(strs)):
                if  si >= len(strs[i]) or si >= len(lcp) or strs[i][si] != lcp[si]:
                    return lcp[:si]
            si += 1    

