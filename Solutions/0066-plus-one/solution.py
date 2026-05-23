class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer_form = int("".join([str(digit) for digit in digits])) + 1
        return [integer for integer in str(integer_form)]
