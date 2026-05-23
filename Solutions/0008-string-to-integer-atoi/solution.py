class Solution:
    def myAtoi(self, s: str) -> int:
        ret = 0

        offset = 0
        while offset < len(s) and s[offset] == ' ':
            offset += 1

        neg = 0
        if offset >= len(s):
            return 0
        if s[offset] == '-':
            offset += 1
            neg = 1
        elif s[offset] == '+':
            offset += 1

        while offset < len(s) and s[offset] == '0':
            offset += 1

        z = ord('0')
        for i in range(offset, len(s)):
            if not s[i].isdigit():
                break
            ret = (ret * 10) + (ord(s[i]) - z)
        ret = -1 * ret if neg else ret

        bounds = [-2 ** 31, (2 ** 31) - 1]
        if ret < bounds[0]:
            return bounds[0]
        elif ret > bounds[1]:
            return bounds[1]
        else:
            return ret

