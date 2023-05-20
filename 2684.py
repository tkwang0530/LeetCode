"""
2684. Maximum Number of Moves in a Grid
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.

Example1:
Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.

Example2:
Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.

Constraints:
m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 10^5
1 <= grid[i][j] <= 10^6
"""

"""
Note:
1. dp: O(mn) time | O(mn) space - where n is the width of the matrix grid and m is the height of the matrix grid
"""

import unittest
from typing import List
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[False] * cols for _ in range(rows)]
        for row in range(rows):
            dp[row][0] = True

        maxCol = 0
        for col in range(cols):
            prevCol = maxCol
            for row in range(rows):
                if not dp[row][col]:
                    continue

                currentVal = grid[row][col]
                for nextRow, nextCol in [(row-1,col+1), (row, col+1), (row+1, col+1)]:
                    if nextRow in (-1, rows) or nextCol in (-1, cols):
                        continue
                    nextVal = grid[nextRow][nextCol]
                    if nextVal > currentVal:
                        dp[nextRow][nextCol] = True
                        maxCol = max(maxCol, nextCol)
            if prevCol == maxCol:
                break
        return maxCol

    def MaxMoves2(self, tiles: str) -> int:
        def dfs(charCounts):
            total = 0
            for i in range(len(charCounts)):
                if charCounts[i] > 0:
                    total += 1
                    charCounts[i] -= 1
                    total += dfs(charCounts)
                    charCounts[i] += 1
            return total
        
        charIdx = {}
        idx = 0
        charCounts = []
        for char in tiles:
            if char not in charIdx:
                charIdx[char] = idx
                charCounts.append(0)
                idx += 1
            charCounts[charIdx[char]] += 1
        
        return dfs(charCounts)

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
