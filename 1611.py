"""
1611. Minimum One Bit Operations to Make Integers Zero
description: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/
"""

"""
Note:
1. dfs+memo: O(logn) time | O(logn) space
"""

import functools
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(n) -> int:
            if n == 0:
                return 0
            b = 1
            while (b << 1) <= n:
                b = b << 1
            return dfs((b >> 1) ^ b ^ n) + 1 + b - 1
        return dfs(n)

# Unit Tests
import unittest
funcs = [Solution().minimumOneBitOperations]

class TestMinimumOneBitOperations(unittest.TestCase):
    def testMinimumOneBitOperations1(self):
        for minimumOneBitOperations in funcs:
            n=3
            self.assertEqual(minimumOneBitOperations(n=n), 2)

    def testMinimumOneBitOperations2(self):
        for minimumOneBitOperations in funcs:
            n=6
            self.assertEqual(minimumOneBitOperations(n=n), 4)

if __name__ == "__main__":
    unittest.main()