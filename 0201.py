"""
201. Bitwise AND of Numbers Range
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example1:
Input: left = 5, right = 7
Output: 4

Example2:
Input: left = 0, right = 0
Output: 0

Example3:
Input: left = 1, right = 2147483647
Output: 0

Constraints:
0 <= left <= right <= 2^31 - 1
"""

"""
Note:
1. Bit Manipulation using >>, << operator: O(1) time | O(1) space
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            count += 1
        return left << count


# Unit Tests
import unittest
funcs = [Solution().rangeBitwiseAnd]

class TestRangeBitwiseAnd(unittest.TestCase):
    def testRangeBitwiseAnd1(self):
        for func in funcs:
            left = 5
            right = 7
            self.assertEqual(func(left=left, right=right), 4)

    def testRangeBitwiseAnd2(self):
        for func in funcs:
            left = 0
            right = 0
            self.assertEqual(func(left=left, right=right), 0)

    def testRangeBitwiseAnd3(self):
        for func in funcs:
            left = 1
            right = 2147483647
            self.assertEqual(func(left=left, right=right), 0)

if __name__ == "__main__":
    unittest.main()
