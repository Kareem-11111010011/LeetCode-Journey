class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag1 = {}
        flag2 = {}
        
        for char in s:
            if char in flag1:
                flag1[char] += 1
            else:
                flag1[char] = 1
        for char in t:
            if char in flag2:
                flag2[char] += 1
            else:
                flag2[char] = 1

        return False if flag1 != flag2 else True
