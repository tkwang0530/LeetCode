"""
1551. Minimum Operations to Make Array Equal
description: https://leetcode.com/problems/minimum-operations-to-make-array-equal/description/
"""

"""
Note:
1. Math: O(1) time | O(1) space
"""

class Solution:
    def minOperations(self, n: int) -> int:
        top = n - 1
        bottom = 1 if n % 2 == 0 else 0
        h = (top - bottom) // 2 + 1
        return (top + bottom) * h // 2

# Unit Tests
import unittest
funcs = [Solution().minOperations]
class TestMinOperations(unittest.TestCase):
    def testMinOperations1(self):
        for minOperations in funcs:
            n = 3
            self.assertEqual(minOperations(n=n), 2)

    def testMinOperations2(self):
        for minOperations in funcs:
            n = 6
            self.assertEqual(minOperations(n=n), 9)

if __name__ == "__main__":
    unittest.main()
