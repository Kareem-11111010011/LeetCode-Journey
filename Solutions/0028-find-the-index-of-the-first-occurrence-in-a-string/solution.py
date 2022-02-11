class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_index = 0
        if not needle:
            return 0
        for c in haystack:
            if needle not in haystack:
                continue
        haystack_index = haystack.index(needle) if needle in haystack else -1
        return (haystack_index)
