"""
695. Max Area of Island
You are given an m x n binary matrix grid. An island is a group of 1's (land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example1:
Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""

"""
Note:
1. Recursion (DFS): O(nm) time | O(nm) space
using [area, maxArea]
2. Iteration (BFS): O(nm) time | O(nm) space
using [area, maxArea]
"""




from collections import deque
from typing import List
import unittest
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = [0, 0]  # area, maxArea
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    result[0] += 1
                    self.dfs(grid, row, col, result)
                    result[1] = max(result[1], result[0])
                    result[0] = 0
        return result[1]

    def dfs(self, grid, row, col, result):
        grid[row][col] = 0
        directions = [(row - 1, col), (row + 1, col),
                      (row, col + 1), (row, col - 1)]
        for x, y in directions:
            if not self.isWater(grid, x, y):
                result[0] += 1
                self.dfs(grid, x, y, result)

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        result = [0, 0]  # [area, maxArea]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    result[0] += 1
                    self.bfs(grid, row, col, result)
                    result[1] = max(result[1], result[0])
                    result[0] = 0
        return result[1]

    def bfs(self, grid, row, col, result):
        queue = deque([(row, col)])
        grid[row][col] = 0
        while queue:
            r, c = queue.popleft()
            directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for x, y in directions:
                if not self.isWater(grid, x, y):
                    result[0] += 1
                    grid[x][y] = 0
                    queue.append((x, y))

    def isWater(self, grid, row, col):
        return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0


# Unit Tests
funcs = [Solution().maxAreaOfIsland, Solution().maxAreaOfIsland2]


class TestMaxAreaOfIsland(unittest.TestCase):
    def testMaxAreaOfIsland1(self):
        for func in funcs:
            grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
                0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
            self.assertEqual(func(grid=grid), 6)

    def testMaxAreaOfIsland2(self):
        for func in funcs:
            grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
            self.assertEqual(func(grid=grid), 0)


if __name__ == "__main__":
    unittest.main()
