"""
263. Ugly Number
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:
-2^31 <= n <= 2^31 - 1
"""

"""
Note:
1. Brute-Force: O(logn) time | O(1) space
"""




import unittest
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        return n == 1


# Unit Tests
funcs = [Solution().isUgly]


class TestIsUgly(unittest.TestCase):
    def testIsUgly1(self):
        for func in funcs:
            self.assertEqual(func(n=6), True)

    def testIsUgly2(self):
        for func in funcs:
            self.assertEqual(func(n=1), True)

    def testIsUgly3(self):
        for func in funcs:
            self.assertEqual(func(n=14), False)


if __name__ == "__main__":
    unittest.main()
