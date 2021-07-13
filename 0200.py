"""
200. Number of Islands
Given an m x n 2D binary grid which represents a map of "1"s (land) and "0"s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assum all four edges of the grid are all surrounded by water.

Example1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

"""
Note:
1. Recursion (DFS): O(nm) time | O(nm) space
2. Iteration (BFS): O(nm) time | O(nm) space
"""




from collections import deque
from typing import List
import unittest
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge
        if not grid:
            return 0
        numOfIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    numOfIslands += 1
        return numOfIslands

    def dfs(self, grid, row, col):
        if self.isWater(grid, row, col):
            return
        grid[row][col] = "0"
        directions = [(row - 1, col), (row + 1, col),
                      (row, col + 1), (row, col - 1)]
        for x, y in directions:
            self.dfs(grid, x, y)

    def numIslands2(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        numOfIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    self.bfs(grid, row, col)
                    numOfIslands += 1
        return numOfIslands

    def bfs(self, grid, row, col):
        queue = deque([(row, col)])
        while queue:
            currentRow, currentCol = queue.popleft()
            directions = [(currentRow + 1, currentCol), (currentRow - 1, currentCol),
                          (currentRow, currentCol + 1), (currentRow, currentCol - 1)]
            for x, y in directions:
                if not self.isWater(grid, x, y):
                    queue.append((x, y))
                    grid[x][y] = "0"

    def isWater(self, grid, row, col):
        return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0"


# Unit Tests
funcs = [Solution().numIslands, Solution().numIslands2]


class TestNumIslands(unittest.TestCase):
    def testNumIslands1(self):
        for func in funcs:
            grid = [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ]
            self.assertEqual(func(grid=grid), 3)

    def testNumIslands2(self):
        for func in funcs:
            grid = [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ]
            self.assertEqual(func(grid=grid), 1)


if __name__ == "__main__":
    unittest.main()
