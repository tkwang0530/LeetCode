"""
343. Integer Break
description: https://leetcode.com/problems/integer-break/description/
"""

"""
Note:
1. dp+memo: O(n) time | O(n) space
"""

import functools
class Solution:
    def integerBreak(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(n) -> int:
            if n == 1:
                return 1
            maxProduct = 1
            for i in range(1, n+1):
                maxProduct = max(maxProduct, i * dfs(n-i))
            return maxProduct
        
        maxProduct = 1
        for i in range(1, n):
            maxProduct = max(maxProduct, i * dfs(n-i))
        return maxProduct

# Unit Tests
import unittest
funcs = [Solution().integerBreak]

class TestIntegerBreak(unittest.TestCase):
    def testIntegerBreak1(self):
        for IntegerBreak in funcs:
            n = 2
            self.assertEqual(IntegerBreak(n=n), 1)

    def testIntegerBreak2(self):
        for IntegerBreak in funcs:
            n = 10
            self.assertEqual(IntegerBreak(n=n), 36)

if __name__ == "__main__":
    unittest.main()