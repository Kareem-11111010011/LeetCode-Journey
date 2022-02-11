class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for count,char in enumerate(reversed(s.strip()), 1):
            if char == " ":
                count = count - 1
                break
        return count
