"""
361. Bomb Enemy
Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.

The bomb kills all the enemis in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.

Example1:
Input: grid = [["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]
Output: 3

Example2:
Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
Output: 1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 'W', 'E', or '0'
"""

""" 
Note:
1. Hash Table: O(nm) time | O(m) space, where n is row length and m is col length
calculate enemies using expension, break for the wall
calculateRowEnemies using int variable
calculateColEnemies using dictionary
"""

from typing import List
class Solution(object):
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        enemiesInRow = 0
        enemiesInColDict = {}
        maxKilled = 0
        for row in range(len(grid)):
            enemiesInRow = 0
            for col in range(len(grid[row])):
                if grid[row][col] == "0": # empty
                    if enemiesInRow == 0:
                        enemiesInRow = self.calculateRowEnemies(grid, row, col)
                    if col not in enemiesInColDict:
                        enemiesInColDict[col] = self.calculateColEnemies(grid, row, col)
                    rowEnemies, colEnemies = enemiesInRow, enemiesInColDict[col]
                    maxKilled = max(maxKilled, rowEnemies + colEnemies)
                elif grid[row][col] == "W":
                    enemiesInRow = 0
                    if col in enemiesInColDict:
                        del enemiesInColDict[col]
        return maxKilled

    def calculateRowEnemies(self, grid, row, col):
        left, right = col-1, col+1
        enemies = 0
        while left >= 0:
            if grid[row][left] == "W":
                break
            if grid[row][left] == "E":
                enemies += 1
            left -= 1
        while right < len(grid[0]):
            if grid[row][right] == "W":
                break
            if grid[row][right] == "E":
                enemies += 1
            right += 1
        return enemies

    def calculateColEnemies(self, grid, row, col):
        up, down = row-1, row+1
        enemies = 0
        while up >= 0:
            if grid[up][col] == "W":
                break
            if grid[up][col] == "E":
                enemies += 1
            up -= 1
        while down < len(grid):
            if grid[down][col] == "W":
                break
            if grid[down][col] == "E":
                enemies += 1
            down += 1
        return enemies


# Unit Tests
import unittest
funcs = [Solution().maxKilledEnemies]

class TestMaxKilledEnemies(unittest.TestCase):
    def testMaxKilledEnemies1(self):
        for func in funcs:
            grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
            self.assertEqual(func(grid=grid), 3)

    def testMaxKilledEnemies2(self):
        for func in funcs:
            grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
            self.assertEqual(func(grid=grid), 1)

    def testMaxKilledEnemies3(self):
        for func in funcs:
            grid = [["0","0","0","0","E"],["W","E","E","E","E"],["E","E","0","E","0"],["W","E","E","E","E"],["W","W","W","W","W"]]
            self.assertEqual(func(grid=grid), 6)

    def testMaxKilledEnemies4(self):
        for func in funcs:
            grid = [["W","W","W","W","E","0","E","0","E","0","E"],["W","E","E","E","E","0","0","0","0","0","0"],["E","E","0","E","0","E","E","E","E","E","E"],["W","E","E","E","E","0","0","0","0","0","0"],["0","0","0","0","0","E","E","E","E","E","E"]]
            self.assertEqual(func(grid=grid), 12)

if __name__ == "__main__":
    unittest.main()
