"""
7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Examples:
    Given 123, the answer is 321.
    Given -123, the answer is -321.
    Given 0, the answer is 0.
"""

"""
Note:
1. Convert to String then reverse it: O(1) time | O(1) space
2. Bit Manipulation: O(1) time | O(1) space
"""

import math
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        result = sign * int(str(abs(x))[::-1])
        return result if -(2 ** 31) - 1 < result < 2 ** 31 else 0

    def reverse2(self, x: int) -> int:
        MIN = -2 ** 31
        MAX = 2 ** 31 - 1
        result = 0
        while x:
            digit = int(math.fmod(x, 10))     # (python dumb) -1 % 10 = 9
            x = int(x / 10)                             # (python dumb) -1 // 10 = -1
            if (result > MAX // 10 or
                (result == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (result < MIN // 10 or
                (result == MIN // 10 and digit <= MIN % 10)):
                return 0
            result = result * 10 + digit
        return result


# Unit Tests
import unittest
funcs = [Solution().reverse, Solution().reverse2]

class TestReverseInteger(unittest.TestCase):
    def testReverseInteger1(self):
        for func in funcs:
            self.assertEqual(func(x=123), 321)

    def testReverseInteger2(self):
        for func in funcs:
            self.assertEqual(func(x=-123), -321)

    def testReverseInteger3(self):
        for func in funcs:
            self.assertEqual(func(x=0), 0)

if __name__ == "__main__":
    unittest.main()
