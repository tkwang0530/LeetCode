"""
2373. Largest Local Values in a Matrix
description: https://leetcode.com/problems/largest-local-values-in-a-matrix/description/
"""

"""
Note:
1. Brute-Force: O(9*(n-2)^2) time | O(1) space - where n is the length of grid[0]
"""

from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        maxLocal = [[0] * (cols-2) for _ in range(rows-2)]

        def getLocalMax(row, col) -> int:
            maxVal = 0
            for rowDiff in range(-1, 2, 1):
                for colDiff in range(-1, 2, 1):
                    r = row+rowDiff
                    c = col+colDiff
                    maxVal = max(maxVal, grid[r][c])
            return maxVal

        for row in range(1, rows-1):
            for col in range(1, cols-1):
                localMax = getLocalMax(row, col)
                maxLocal[row-1][col-1] = localMax

        return maxLocal

# Unit Tests
import unittest
funcs = [Solution().largestLocal]


class TestLargestLocal(unittest.TestCase):
    def testLargestLocal1(self):
        for func in funcs:
            grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
            self.assertEqual(func(grid=grid), [[9,9],[8,6]])


    def testLargestLocal2(self):
        for func in funcs:
            grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
            self.assertEqual(func(grid=grid), [[2,2,2],[2,2,2],[2,2,2]])


if __name__ == "__main__":
    unittest.main()