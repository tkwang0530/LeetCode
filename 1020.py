"""
1020. Number of Enclaves
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

Constraints:
m == grid.length
n == grid.length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""

"""
Note:
1. DFS: O(mn) time | O(mn) space - where m is len(grid) and n is len(grid[i])
"""
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(row, col):
            if row in (-1, m) or col in (-1, n) or grid[row][col] == 0:
                return
            grid[row][col] = 0
            for x, y in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                dfs(x, y)
    
        for col in range(n):
            dfs(0, col)
            dfs(m-1, col)
            
        for row in range(m):
            dfs(row, 0)
            dfs(row, n-1)
            
        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    res += 1
        return res

# Unit Tests
import unittest
funcs = [Solution().numEnclaves]
class TestNumEnclaves(unittest.TestCase):
    def testNumEnclaves1(self):
        for func in funcs:
            grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
            self.assertEqual(func(grid=grid), 3)

    def testNumEnclaves2(self):
        for func in funcs:
            grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
            self.assertEqual(func(grid=grid), 0)

if __name__ == "__main__":
    unittest.main()
