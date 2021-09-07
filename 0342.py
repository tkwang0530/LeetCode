"""
342. Power of Four
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4^x

Example1:
Input: n = 16
Output: true

Example2:
Input: n = 5
Output: false

Example3:
Input: n = 1
Output: true

Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""

"""
Note:
1. Iteration: O(1) time | O(1) space
"""

import unittest
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 4:
            return False
        while n % 4 == 0:
            n = n // 4
        return n == 1

# Unit Tests
funcs = [Solution().isPowerOfFour]


class TestIsPowerOfFour(unittest.TestCase):
    def testIsPowerOfFour1(self):
        for func in funcs:
            self.assertEqual(func(n=16), True)

    def testIsPowerOfFour2(self):
        for func in funcs:
            self.assertEqual(func(n=5), False)

    def testIsPowerOfFour3(self):
        for func in funcs:
            self.assertEqual(func(n=1), True)

if __name__ == "__main__":
    unittest.main()
