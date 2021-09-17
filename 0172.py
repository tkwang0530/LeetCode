"""
172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n! .

Follow up: Could you write a solution that works in logarithmic time complexity?

Example1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example3:
Input: n = 0
Output: 0

Constraints:
0 <= n <= 10^4
"""

"""
Notes:
1. Divide and increment: O(n) time | O(1) space
2. Recursion: O(logn) time | O(logn) space
Because all trailing 0 is from factors 5 * 2.
But sometimes one number may have several 5 factors, 25 has two 5 factors, 125 have three 5 factors.
In the n! operation, factors 2 is always sufficient. So we just count how many 5 factors in all number from 1 to n
e.g. n = 125
125 // 5 = 25 # from 0~125 there are 25 numbers have at least one 5 factor
125 // 25 = 5 # from 0~125 there are 5 numbers have at least two 5 factors
125 // 125 = 1 # from 0~125 there are 1 number has at least three 5 factors
25 + 5 + 1 = 31

3. Iteration: O(logn) time | O(1) space
"""
class Solution(object):
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        tempNumber = 1
        zeroes = 0
        while n > 0:
            tempNumber *= n
            while tempNumber % 10 == 0:
                tempNumber = tempNumber // 10
                zeroes += 1
            n -= 1
        return zeroes
    
    def trailingZeroes2(self, n: int) -> int:
        return 0 if n == 0 else n // 5 + self.trailingZeroes2(n // 5)

    def trailingZeroes3(self, n: int) -> int:
        count = 0
        powerOfFive = 1
        while n // (5 ** powerOfFive) > 0:
            count += n // (5 ** powerOfFive)
            powerOfFive += 1
        return count


# Unit Tests
import unittest
funcs = [Solution().trailingZeroes, Solution().trailingZeroes2, Solution().trailingZeroes3]

class TestTrailingZeroes(unittest.TestCase):
    def testTrailingZeroes1(self):
        for func in funcs:
            self.assertEqual(func(n=3), 0)

    def testTrailingZeroes2(self):
        for func in funcs:
            self.assertEqual(func(n=5), 1)

    def testTrailingZeroes3(self):
        for func in funcs:
            self.assertEqual(func(n=0), 0)


if __name__ == "__main__":
    unittest.main()