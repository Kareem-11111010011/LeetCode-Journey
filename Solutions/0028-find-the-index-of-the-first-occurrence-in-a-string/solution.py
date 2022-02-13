class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_index = 0
        if not needle:
            return 0
        haystack_index = haystack.index(needle) if needle in haystack else -1
        return (haystack_index)
