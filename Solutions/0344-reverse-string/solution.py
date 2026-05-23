class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for char in s[::-1]:
            s.pop(0)
            s.append(char)
