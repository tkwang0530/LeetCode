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
1. Convert to String then reverse it: O(n) time | O(1) space
"""




import unittest
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        result = sign * int(str(abs(x))[::-1])
        return result if -(2 ** 31) - 1 < result < 2 ** 31 else 0


# Unit Tests


class TestReverseInteger(unittest.TestCase):
    def testReverseInteger1(self):
        func = Solution().reverse
        self.assertEqual(func(x=123), 321)

    def testReverseInteger2(self):
        func = Solution().reverse
        self.assertEqual(func(x=-123), -321)

    def testReverseInteger3(self):
        func = Solution().reverse
        self.assertEqual(func(x=0), 0)


if __name__ == "__main__":
    unittest.main()
