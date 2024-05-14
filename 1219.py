"""
1219. Path with Maximum Gold
description: https://leetcode.com/problems/path-with-maximum-gold/description/
"""

"""
Note:
1. dfs: O(mn * 4^25) time | O(mn) space - where m is the number of rows in the grid and n is the number of columns in the grid
"""

import unittest
from typing import List
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row, col):
            collected = 0
            for nextRow, nextCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if nextRow in (-1, rows) or nextCol in (-1, cols):
                    continue

                if grid[nextRow][nextCol] == 0:
                    continue
                
                gold = grid[nextRow][nextCol] 
                grid[nextRow][nextCol] = 0
                collected = max(collected, gold+dfs(nextRow, nextCol))
                grid[nextRow][nextCol] = gold
            return collected

        maxCollected = 0
        for row in range(rows):
            for col in range(cols):
                gold = grid[row][col]
                if gold > 0:
                    grid[row][col] = 0
                    maxCollected = max(maxCollected, gold+dfs(row, col))
                    grid[row][col] = gold
        return maxCollected

# Unit Tests
import unittest
funcs = [Solution().getMaximumGold]
class TestGetMaximumGold(unittest.TestCase):
    def testGetMaximumGold1(self):
        for func in funcs:
            grid = [[0,6,0],[5,8,7],[0,9,0]]
            self.assertEqual(func(grid), 24)

    def testGetMaximumGold2(self):
        for func in funcs:
            grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
            self.assertEqual(func(grid), 28)

if __name__ == "__main__":
    unittest.main()
