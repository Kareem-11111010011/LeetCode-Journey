class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "".join(char for char in s if char.isalnum()).lower()
        return (alphanumeric == alphanumeric[::-1])
