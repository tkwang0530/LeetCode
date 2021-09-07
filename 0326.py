"""
326. Power of Three
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example1:
Input: n = 27
Output: true

Example2:
Input: n = 0
Output: false

Example3:
Input: n = 9
Output: true

Example4:
Input: n = 45
Output: false

Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""

"""
Note:
1. Iteration: O(1) space | O(1) time
2. Recursion: O(1) space | O(1) time
"""

import unittest
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n <= 2:
            return False
        while n > 3:
            if n % 3 == 0:
                n /= 3
            else:
                return False
        return n == 3
    
    def isPowerOfThree2(self, n: int) -> bool:
        return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree2(n // 3)))



# Unit Tests
funcs = [Solution().isPowerOfThree, Solution().isPowerOfThree2]


class TestIsPowerOfThree(unittest.TestCase):
    def testIsPowerOfThree1(self):
        for func in funcs:
            self.assertEqual(func(n=27), True)

    def testIsPowerOfThree2(self):
        for func in funcs:
            self.assertEqual(func(n=0), False)

    def testIsPowerOfThree3(self):
        for func in funcs:
            self.assertEqual(func(n=9), True)

    def testIsPowerOfThree4(self):
        for func in funcs:
            self.assertEqual(func(n=45), False)

if __name__ == "__main__":
    unittest.main()
