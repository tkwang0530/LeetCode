"""
463. Island Perimeter
You are given row x col grid representing a map where grid[i][j] = 1
represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e, one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example1:
Input: grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.


Example2:
Input: grid = [[1]]
Output: 4

Example3:
Input: grid = [[1,0]]
Output: 4

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
"""

"""
Note:
1. Recursive DFS: O(nm) time | O(nm) space
2. Count islands and neighbors: O(nm) time | O(1) space
perimeter = 4 * islands - 2 * neighbors
"""

from typing import List
import unittest
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        result = [0] # [perimeter]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    self.dfs(grid, row, col, visited, result)
                    return result[0]
    
    def dfs(self, grid, row, col, visited, result) -> None:
        if self.isWater(grid, row, col):
            result[0] += 1
            return
        if (row, col) in visited:
            return
        visited.add((row, col))
        directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for row, col in directions:
            self.dfs(grid, row, col, visited, result)

    def isWater(self, grid, row, col) -> bool:
        return row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == 0


    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        islands = neighbors = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    islands += 1
                    if row < len(grid) - 1 and grid[row + 1][col] == 1:
                        neighbors += 1
                    if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
                        neighbors += 1
        return islands * 4 - neighbors * 2

# Unit Tests
funcs = [Solution().islandPerimeter, Solution().islandPerimeter2]


class TestIslandPerimeter(unittest.TestCase):
    def testIslandPerimeter1(self):
        for func in funcs:
            grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
            self.assertEqual(func(grid=grid), 16)

    def testIslandPerimeter2(self):
        for func in funcs:
            grid = [[1]]
            self.assertEqual(func(grid=grid), 4)

    def testIslandPerimeter3(self):
        for func in funcs:
            grid = [[1,0]]
            self.assertEqual(func(grid=grid), 4)

if __name__ == "__main__":
    unittest.main()
