"""
1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0
Given n , return the value of Tn

Example1:
Input: n = 4
Output: 4
"""

"""
Note:
1. Recursion
O(3^n) time | O(n) space

2. Iteration
"""

from typing import List


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

    def tribonacci2(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for i in range(n):
            a, b, c = b, c, a + b + c
        return a


# Unit Tests
import unittest


class TestTribonacci(unittest.TestCase):
    def testTribonacci1(self):
        func = Solution().tribonacci
        func2 = Solution().tribonacci2
        self.assertEqual(func(n=4), 4)
        self.assertEqual(func2(n=4), 4)


if __name__ == "__main__":
    unittest.main()