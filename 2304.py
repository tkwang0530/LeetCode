
"""
2304. Minimum Path Cost in a Grid
description: https://leetcode.com/problems/minimum-path-cost-in-a-grid/description/
"""

"""
Note:
1. dfs+memo: O(m*n*n) time | O(m*n) space - where m is len(grid) and n is len(grid[0])
"""

from typing import List
import functools
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        @functools.lru_cache(None)
        def dfs(row, col):
            if row == rows-1:
                return grid[row][col]

            minCost = float("inf")
            val = grid[row][col]
            for nextCol, cost in enumerate(moveCost[val]):
                minCost = min(minCost, val + cost + dfs(row+1, nextCol))
            return minCost

        return min([dfs(0, i) for i in range(cols)])

# Unit Tests
import unittest
funcs = [Solution().minPathCost]

class TestMinPathCost(unittest.TestCase):
    def testMinPathCost1(self):
        for minPathCost in funcs:
            grid = [[5,3],[4,0],[2,1]]
            moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
            self.assertEqual(minPathCost(grid=grid, moveCost=moveCost), 17)


    def testMinPathCost2(self):
        for minPathCost in funcs:
            grid = [[5,1,2],[4,0,3]]
            moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]
            self.assertEqual(minPathCost(grid=grid, moveCost=moveCost), 6)

if __name__ == "__main__":
    unittest.main()