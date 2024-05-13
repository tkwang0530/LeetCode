"""
861. Score After Flipping Matrix
description: https://leetcode.com/problems/score-after-flipping-matrix/description/
"""

"""
Note:
1. Greedy: O(mn) time | O(1) space - where m is the number of rows and n is the number of columns
"""

import unittest
from typing import List
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        highest = rows * (2 ** (cols-1))
        for col in range(1, cols):
            maxCount = 0
            for r in range(rows):
                if grid[r][col] != grid[r][0]:
                    maxCount += 1
            maxCount = max(maxCount, rows-maxCount)
            highest += maxCount * (2 ** (cols-col-1))
        return highest

# Unit Tests
import unittest
funcs = [Solution().matrixScore]
class TestMatrixScore(unittest.TestCase):
    def testMatrixScore1(self):
        for func in funcs:
            grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
            self.assertEqual(func(grid), 39)

    def testMatrixScore2(self):
        for func in funcs:
            grid = [[0]]
            self.assertEqual(func(grid), 1)

if __name__ == "__main__":
    unittest.main()
