"""
1568. Minimum Number of Days to Disconnect Island
description: https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/
"""

""" 
1. Greedy + DFS: O(m^2*n^2) time | O(mn) space - where m is len(grid) and n is len(grid[0])
"""

from typing import List
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row, col, visited):
            for nextRow, nextCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if nextRow in (-1, rows) or nextCol in (-1, cols):
                    continue

                if grid[nextRow][nextCol] == 0 or (nextRow, nextCol) in visited:
                    continue

                visited.add((nextRow, nextCol))
                dfs(nextRow, nextCol, visited)
        
        def countIsland():
            islands = 0
            visited = set()
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1 and (row, col) not in visited:
                        islands += 1
                        visited.add((row, col))
                        dfs(row, col, visited)
            return islands
        
        islands = countIsland()
        if islands == 0 or islands >= 2:
            return 0
        
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    islands = countIsland()
                    if islands == 0 or islands >= 2:
                        return 1
                    grid[row][col] = 1
        
        return 2

# Unit Tests
import unittest
funcs = [Solution().minDays]


class TestMinDays(unittest.TestCase):
    def testMinDays1(self):
        for minDays in funcs:
            grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
            self.assertEqual(minDays(grid=grid), 2)

    def testMinDays2(self):
        for minDays in funcs:
            grid = [[1,1]]
            self.assertEqual(minDays(grid=grid), 2)

if __name__ == "__main__":
    unittest.main()
