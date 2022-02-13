class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_numeric_s = "".join(filter(str.isalnum, s))
        return (alpha_numeric_s.lower() == alpha_numeric_s[::-1].lower())
