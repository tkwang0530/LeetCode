"""
1254. Number of Closed Islands
Given a 2D grid consists of 0s (land) and 1s (water). An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Example1:
Input: grid = [
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]
]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

Constraints:
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <= 1
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
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = [False, 0]  # [hasTouchedBorder, numberOfClosedIsland]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    result[0] = False
                    self.dfs(grid, row, col, result)
                    if not result[0]:
                        result[1] += 1
        return result[1]

    def dfs(self, grid, row, col, result):
        result[0] = self.isBorder(grid, row, col) or result[0]
        grid[row][col] = 1
        directions = [(row - 1, col), (row + 1, col),
                      (row, col + 1), (row, col - 1)]
        for x, y in directions:
            if not self.isWater(grid, x, y):
                self.dfs(grid, x, y, result)

    def closedIsland2(self, grid: List[List[int]]) -> int:
        result = [False, 0]  # [hasTouchedBorder, numberOfClosedIsland]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    result[0] = False
                    self.bfs(grid, row, col, result)
                    if not result[0]:
                        result[1] += 1
        return result[1]

    def bfs(self, grid, row, col, result):
        result[0] = self.isBorder(grid, row, col) or result[0]
        grid[row][col] = 1
        queue = deque([(row, col)])
        while queue:
            r, c = queue.popleft()
            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for x, y in directions:
                if not self.isWater(grid, x, y):
                    result[0] = self.isBorder(grid, x, y) or result[0]
                    grid[x][y] = 1
                    queue.append((x, y))

    def isWater(self, grid, row, col):
        return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 1

    def isBorder(self, grid, row, col):
        return row <= 0 or col <= 0 or row >= len(grid) - 1 or col >= len(grid[0]) - 1


# Unit Tests
funcs = [Solution().closedIsland, Solution().closedIsland2]


class TestClosedIsland(unittest.TestCase):
    def testClosedIsland1(self):
        for func in funcs:
            grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [
                1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]
            self.assertEqual(func(grid=grid), 2)

    def testClosedIsland2(self):
        for func in funcs:
            grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
            self.assertEqual(func(grid=grid), 1)

    def testClosedIsland3(self):
        for func in funcs:
            grid = [[1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1]]
            self.assertEqual(func(grid=grid), 2)


if __name__ == "__main__":
    unittest.main()
