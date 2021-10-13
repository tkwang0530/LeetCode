"""
69. Sqrt(x)
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example1:
Input: x = 4
Output: 2

Example2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

Constraints:
0 <= x <= 2^32 - 1
"""

"""
Note:
1. Binary Search: O(logn) time | O(1) space
2. Binary Search (prevent over flow logic): O(logn) time | O(1) space
"""

import unittest
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
        return left - 1 # left * left > x

    def mySqrt2(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x+1
        while left < right:
            mid = left + (right - left) // 2
            if x/mid < mid:
                right = mid
            else:
                left = mid + 1
        return left - 1

# Unit Tests
funcs = [Solution().mySqrt, Solution().mySqrt2]

class TestMySqrt(unittest.TestCase):
    def testMySqrt1(self):
        for func in funcs:
            self.assertEqual(
                func(x=4), 2)

    def testMySqrt2(self):
        for func in funcs:
            self.assertEqual(
                func(x=8), 2)

    def testMySqrt3(self):
        for func in funcs:
            self.assertEqual(
                func(x=17), 4)


if __name__ == "__main__":
    unittest.main()
