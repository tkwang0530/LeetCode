"""
1289. Minimum Falling Path Sum II
description: https://leetcode.com/problems/minimum-falling-path-sum-ii/description/
"""

"""
Note:
1. DFS + Greedy + memo: O(3mn) time | O(mn) space - where m is the number of rows and n is the number of columns
"""

import functools, collections, heapq
from typing import List
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rowMin2ColsMap = collections.defaultdict(list) # <row, [(val, col)]>
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                val = grid[row][col]
                if len(rowMin2ColsMap[row]) < 3:
                    heapq.heappush(rowMin2ColsMap[row], (-val, col))
                else:
                    heapq.heappushpop(rowMin2ColsMap[row], (-val, col))

        @functools.lru_cache(None)
        def dfs(row, prevCol) -> int:
            if row == rows:
                return 0
            
            minSum = float("inf")
            for _, col in rowMin2ColsMap[row]:
                if col == prevCol:
                    continue
                minSum = min(minSum, grid[row][col] + dfs(row+1, col))
            return minSum
        
        return dfs(0, -1)
# Unit Tests
import unittest
funcs = [Solution().minFallingPathSum]

class TestMinFallingPathSum(unittest.TestCase):
    def testMinFallingPathSum1(self):
        for func in funcs:
            grid = [[1,2,3],[4,5,6],[7,8,9]]
            self.assertEqual(func(grid=grid), 13)

    def testMinFallingPathSum2(self):
        for func in funcs:
            grid = [[7]]
            self.assertEqual(func(grid=grid), 7)

if __name__ == "__main__":
    unittest.main()