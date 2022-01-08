"""
840. Magic Squares In Grid
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are there? (Each subgrid is contiguous).

Example1:
Input: grid = [
    [4,3,8,4],
    [9,5,1,9],
    [2,7,6,2]
]
Output: 1

Example2:
Input: grid = [[8]]
Output: 0

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
"""

"""
Note:
1. Brute Force: O(nm) time | O(1) space
2. Magic Order: O(nm) time | O(1) space
ref: https://leetcode.com/problems/magic-squares-in-grid/discuss/133874/Python-5-and-43816729
(1) The center of magic square must be 5.
(2) The even must be in the corner, and the odd must be on the edge.
(3) it must be in a order like "43816729" （clockwise or anticlockwise)
"""

from typing import List
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total = 0
        for row in range(rows-2):
            for col in range(cols-2):
                if self.isMagicSquare(row, col, grid):
                    total += 1
        return total

    def isMagicSquare(self, row, col, grid) -> bool:
        squareSet = set()
        for r in range(row, row+3):
            for c in range(col, col+3):
                squareSet.add(grid[r][c])
        if squareSet != {i for i in range(1, 9+1)}:
            return False
        
        for i in range(row, row+3):
            if sum(grid[i][col:col+3]) != 15:
                return False

        for j in range(col, col+3):
            colSum = 0
            for i in range(row, row+3):
                colSum += grid[i][j]
            if colSum != 15:
                return False
        
        if sum([grid[row][col], grid[row+1][col+1], grid[row+2][col+2]]) != 15:
            return False
        if sum([grid[row][col+2], grid[row+1][col+1], grid[row+2][col]]) != 15:
            return False
        return True

    def numMagicSquaresInside2(self, grid: List[List[int]]) -> int:
        def isMagicSquare(row, col):
            s = "".join(str(grid[row+x//3][col+x%3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return grid[row][col] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)
        
        rows, cols = len(grid), len(grid[0])
        total = 0
        for row in range(rows-2):
            for col in range(cols-2):
                if isMagicSquare(row, col) and grid[row+1][col+1] == 5:
                    total += 1
        return total

# Unit Tests
import unittest
funcs = [Solution().numMagicSquaresInside, Solution().numMagicSquaresInside2]

class TestNumMagicSquaresInside(unittest.TestCase):
    def testNumMagicSquaresInside1(self):
        for func in funcs:
            grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
            self.assertEqual(func(grid=grid), 1)

    def testNumMagicSquaresInside2(self):
        for func in funcs:
            grid = [[8]]
            self.assertEqual(func(grid=grid), 0)

    def testNumMagicSquaresInside3(self):
        for func in funcs:
            grid = [[5,5,5],[5,5,5],[5,5,5]]
            self.assertEqual(func(grid=grid), 0)


if __name__ == "__main__":
    unittest.main()