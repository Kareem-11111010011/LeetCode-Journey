class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def helper(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False

            if s[i] == t[j]:
                return helper(i+1, j+1)
            else:
                return helper(i, j+1)
        return helper(0, 0)
