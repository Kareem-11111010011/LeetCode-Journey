class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sd = {}
        for char in s:
            sd[char] = sd.get(char, 0) + 1
        
        td = {}
        for char in t:
            td[char] = td.get(char, 0) + 1
        
        return sd == td
