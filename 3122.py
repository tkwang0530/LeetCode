"""
3122. Minimum Number of Operations to Satisfy Conditions
description: https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/description/
"""

"""
Note:
1. dfs + memo + hashTable: O(100n + mn) time | O(20n) space - where m is grid length and n is grid width
"""

from typing import List
import collections, functools
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        colCounters = [collections.defaultdict(int) for _ in range(len(grid[0]))]
        for row in range(rows):
            for col in range(cols):
                val = grid[row][col]
                colCounters[col][val] += 1
                colCounters[col][-1] = 0
                
        
        @functools.lru_cache(None)
        def dfs(col, preVal):
            if col == cols:
                return 0
            minOps = float("inf")
            for num in colCounters[col].keys():
                if num == preVal:
                    continue
                minOps = min(minOps, (rows-colCounters[col][num]) + dfs(col+1, num))
            return minOps
        
        return dfs(0, -1)

# Unit Tests
import unittest
funcs = [Solution().minimumOperations]
class TestMinimumOperations(unittest.TestCase):
    def testMinimumOperations1(self):
        for func in funcs:
            grid = [[1,0,2],[1,0,2]]
            self.assertEqual(func(grid), 0)


    def testMinimumOperations2(self):
        for func in funcs:
            grid = [[1,1,1],[0,0,0]]
            self.assertEqual(func(grid), 3)

    def testMinimumOperations3(self):
        for func in funcs:
            grid = [[1],[2],[3]]
            self.assertEqual(func(grid), 2)


if __name__ == "__main__":
    unittest.main()
