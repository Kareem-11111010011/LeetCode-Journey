class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if not s else len(s.split()[-1])
