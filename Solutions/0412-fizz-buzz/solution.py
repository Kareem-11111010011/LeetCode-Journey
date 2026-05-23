class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        Fizz_Buzz = 15
        Fizz = 3
        Buzz = 5
        for num in range(1, n + 1):
            if num == Fizz_Buzz:
                output.append("FizzBuzz")
                Fizz += 3
                Buzz += 5
                Fizz_Buzz += 15
            elif num == Fizz:
                output.append("Fizz")
                Fizz += 3
            elif num == Buzz:
                output.append("Buzz")
                Buzz += 5
            else:
                output.append(str(num))
        return output
