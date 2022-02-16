class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = int("".join([str(ints) for ints in digits])) + 1
        return [digit for digit in str(answer)]
