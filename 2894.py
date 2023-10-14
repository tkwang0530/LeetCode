"""
2894. Divisible and Non-divisible Sums Difference
description: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/
"""

"""
Note:
1. math: O(1) time | O(1) space
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        totalSum = (1+n) * n // 2
        k = n // m
        a1 = m
        an = a1+m*(k-1)
        num2 = (a1+an)*k//2
        num1 = totalSum - num2
        return num1 - num2

# Unit Tests
import unittest
funcs = [Solution().differenceOfSums]

class TestDifferenceOfSums(unittest.TestCase):
    def testDifferenceOfSums1(self):
        for func in funcs:
            n = 10
            m = 3
            self.assertEqual(func(n=n, m=m), 19)

    def testDifferenceOfSums2(self):
        for func in funcs:
            n = 5
            m = 6
            self.assertEqual(func(n=n, m=m), 15)

    def testDifferenceOfSums3(self):
        for func in funcs:
            n = 5
            m = 1
            self.assertEqual(func(n=n, m=m), -15)

if __name__ == "__main__":
    unittest.main()