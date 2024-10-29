"""
2684. Maximum Number of Moves in a Grid
description: https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/
"""

"""
Note:
1. dp (1D): O(mn) time | O(m) space - where m and n are the dimension of the grid
"""

from typing import List
import unittest, collections
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp0 = collections.defaultdict(int)
        maxSteps = 0
        for col in range(1, cols):
            dp1 = collections.defaultdict(int)
            for row in range(rows):
                val = grid[row][col]
                dp1[row] = max(
                    1+dp0[row-1] if row-1 >= 0 and dp0[row-1] >= 0 and val > grid[row-1][col-1] else -1,
                    1+dp0[row] if dp0[row] >= 0 and val > grid[row][col-1] else -1,
                    1+dp0[row+1] if dp0[row+1] >= 0 and row+1 < rows and val > grid[row+1][col-1] else -1,
                )
                maxSteps = max(maxSteps, dp1[row])
            dp0 = dp1
     
        return maxSteps

# Unit Tests
funcs = [Solution().maxMoves]

class TestMaxMoves(unittest.TestCase):
    def testMaxMoves1(self):
        for func in funcs:
            grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
            self.assertEqual(func(grid=grid), 3)

    def testMaxMoves2(self):
        for func in funcs:
            grid = [[3,2,4],[2,1,9],[1,1,7]]
            self.assertEqual(func(grid=grid), 0)

if __name__ == "__main__":
    unittest.main()
