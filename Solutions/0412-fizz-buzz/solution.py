class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_buzz_list = list(range(1, n + 1))
        for count, num in enumerate(fizz_buzz_list):
            if (num % 3 == 0) & (num % 5 == 0):
                fizz_buzz_list[count] = "FizzBuzz"
            elif num % 3 == 0:
                fizz_buzz_list[count] = "Fizz"
            elif num % 5 == 0:
                fizz_buzz_list[count] = "Buzz"
        return [str(fizz_buzz) for fizz_buzz in fizz_buzz_list]
