"""
96. Unique Binary Search Trees
description: https://leetcode.com/problems/unique-binary-search-trees/description/
"""

"""
Note:
1. DFS + memo: O(n^3) time | O(n^2) space
2. Optimized DFS + memo: O(n^2) time | O(n) space
"""

import functools
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def numTrees(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(lowerBound, upperBound):
            if lowerBound > upperBound:
                return 1
            
            count = 0
            for rv in range(lowerBound, upperBound+1):
                count += dfs(rv+1, upperBound) * dfs(lowerBound, rv-1)
            
            return count

        return dfs(1, n)
    
class Solution2:
    def numTrees(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(n):
            if n <= 1:
                return 1
            
            count = 0
            for rv in range(1, n+1):
                # left: (1 ~ rv-1), right: (rv+1, n)
                count += dfs(rv-1-1+1) * dfs(n-(rv+1)+1)
            
            return count

        return dfs(n)
    
# Unit Tests
import unittest
funcs = [Solution().numTrees, Solution2().numTrees]
class TestNumTrees(unittest.TestCase):
    def testNumTrees1(self):
        for numTrees in funcs:
            n = 3
            self.assertEqual(numTrees(n=n), 5)

    def testNumTrees2(self):
        for NumTrees in funcs:
            n = 1
            self.assertEqual(NumTrees(n=n), 1)

if __name__ == "__main__":
    unittest.main()