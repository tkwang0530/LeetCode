"""
231. Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.

Example1:
Input: n = 1
Output: true
Explanation: 2^0 = 1

Example2:
Input: n = 16
Output: true
Explanation: 2^4 = 16

Example3:
Input: n = 3
Output: false

Example4:
Input: n = 4
Output: true

Example5:
Input: n = 5
Output: false

Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Cound you solve it without loops/recursion?
"""

""" 
1. divided by two: O(1) time | O(1) space
2. Bit Manipulation: O(1) time | O(1) space
2: 10, 1: 01, 2 & 1 = 0
4: 100, 3: 011, 4 & 3 = 0
8: 1000, 7: 0111, 8 & 7 = 0
"""

import unittest
class Solution(object):
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 2 == 0:
            n /= 2
        return True if n == 1 else False

    def isPowerOfTwo2(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0



# Unit Tests
funcs = [Solution().isPowerOfTwo, Solution().isPowerOfTwo2]


class TestIsPowerOfTwo(unittest.TestCase):
    def testIsPowerOfTwo1(self):
        for func in funcs:
            self.assertEqual(func(n=1), True)

    def testIsPowerOfTwo2(self):
        for func in funcs:
            self.assertEqual(func(n=16), True)

    def testIsPowerOfTwo3(self):
        for func in funcs:
            self.assertEqual(func(n=3), False)

    def testIsPowerOfTwo4(self):
        for func in funcs:
            self.assertEqual(func(n=4), True)
    
    def testIsPowerOfTwo5(self):
        for func in funcs:
            self.assertEqual(func(n=5), False)


if __name__ == "__main__":
    unittest.main()
