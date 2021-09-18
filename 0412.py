"""
412. Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:
- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i if non of the above conditions are true.

Example1:
Input: n = 3
Output: ["1","2","Fizz"]

Example2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
1 <= n <= 10^4
"""

"""
Note:
1. mod operation: O(n) time | O(1) space
2. mod operation (neat version): O(n) time | O(1) space
3. without mod operation (faster): O(n) time | O(1) space
"""

from typing import List
class Solution(object):
    def fizzBuzz(self, n: int) -> List[str]:
        result = [i for i in range(1, n+1)]
        for i, num in enumerate(result):
            if num % 15 == 0:
                result[i] = "FizzBuzz"
            elif num % 3 == 0:
                result[i] = "Fizz"
            elif num % 5 == 0:
                result[i] = "Buzz"
            else:
                result[i] = str(num)
        return result
    
    def fizzBuzz2(self, n: int) -> List[str]:
        return [str(i) * (i % 3 != 0 and i % 5 != 0) + "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0 ) for i in range(1, n+1)]

    def fizzBuzz3(self, n: int) -> List[str]:
        result = []
        base3 = 3
        base5 = 5
        base15 = 15
        for i in range(1, n+1):
            if i == base15:
                result.append("FizzBuzz")
                base3 = base15 + 3
                base5 = base15 + 5
                base15 = base15 + 15
            elif i == base3:
                result.append("Fizz")
                base3 += 3
            elif i == base5:
                result.append("Buzz")
                base5 += 5
            else:
                result.append(str(i))
        return result


# Unit Tests
import unittest
funcs = [Solution().fizzBuzz, Solution().fizzBuzz2, Solution().fizzBuzz3]

class TestFizzBuzz(unittest.TestCase):
    def testFizzBuzz1(self):
        for func in funcs:
            n = 3
            self.assertEqual(func(n=n), ["1","2","Fizz"])

    def testFizzBuzz2(self):
        for func in funcs:
            n = 5
            self.assertEqual(func(n=n), ["1","2","Fizz","4","Buzz"])

    def testFizzBuzz3(self):
        for func in funcs:
            n = 15
            self.assertEqual(func(n=n), ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])

if __name__ == "__main__":
    unittest.main()
