class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0] * (n + 1)

        for i in range(0, n + 1):
            ret[i] = bin(i).count('1')
        
        return ret

                
