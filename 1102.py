"""
1102. Path With Maximum Minimum Value
Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the cardinal directions.

The score of a path is the minimum value in that path.
- For example, the score of the path 8 -> 4 -> 5 -> 9 is 4.

Example1:
Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
Output: 4

Example2:
Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2

Example3:
Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
0 <= grid[i][j] <= 10^9
"""

"""
Note:
1. Dijkstra: O(nmlog(nm)) time | O(nm) space - where n, m is len(grid[0]), len(grid)
"""

import unittest, heapq
from typing import List
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maximumScore = grid[0][0]
        maxHeap = [(-1*maximumScore, 0, 0)] # (-value, row, col)
        while maxHeap:
            reversedVal, row, col = heapq.heappop(maxHeap)
            val = reversedVal * -1
            maximumScore = min(maximumScore, val)
            if row == rows-1 and col == cols-1:
                return maximumScore

            grid[row][col] = "*"
            for nextRow, nextCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if nextRow in (-1, rows) or nextCol in (-1, cols):
                    continue

                nextVal = grid[nextRow][nextCol]
                if nextVal == "*":
                    continue

                heapq.heappush(maxHeap, (-1*nextVal, nextRow, nextCol))
        return maximumScore

# Unit Tests
import unittest
funcs = [Solution().maximumMinimumPath]
class TestMaximumMinimumPath(unittest.TestCase):
    def testMaximumMinimumPath1(self):
        for func in funcs:
            grid = [[5,4,5],[1,2,6],[7,4,6]]
            self.assertEqual(func(grid=grid), 4)

    def testMaximumMinimumPath2(self):
        for func in funcs:
            grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
            self.assertEqual(func(grid=grid), 2)

    def testMaximumMinimumPath3(self):
        for func in funcs:
            grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
            self.assertEqual(func(grid=grid), 3)

if __name__ == "__main__":
    unittest.main()
