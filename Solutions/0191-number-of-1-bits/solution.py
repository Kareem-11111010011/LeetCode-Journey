class Solution:
    def hammingWeight(self, n: int) -> int:
        nbin = bin(n)[2:]
        count = 0

        for bit in nbin:
            if bit == '1':
                count = count + 1
        
        return count
