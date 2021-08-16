"""
827. Making a Large Island
You are given an nxn binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1 s.

Example1:
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example2:
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example3:
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""

"""
Note:
1. Recursion (DFS): O(n^2) time | O(n^2) space
2. Recursion (DFS) with List: O(n^2) time | O(n^2) space
"""

from typing import List
import unittest
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # edge check
        if not any(grid):
            return 0
        maxIsland = 0
        islandTag = 2
        areas = {}

        # First Round calculate each island's size and store them into areas dictionary<islandTag, size>
        # islandTag starts from 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    currentIslandArea = self.dfs(grid, row, col, islandTag, 1)
                    maxIsland = max(maxIsland, currentIslandArea)
                    areas[islandTag] = currentIslandArea
                    islandTag += 1

        # Second Round, find each zero, check its neighbors' value, if the neighbor is not water, add it's value(islandTag) into visited set
        # And the sumOfArea = 1(self) + each islands' size from the visited set
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    visited = set()
                    directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                    for row, col in directions:
                        if not self.isWater(grid, row, col):
                            visited.add(grid[row][col])
                    sumOfCurrentIsland = 0
                    for tag in visited:
                        sumOfCurrentIsland += areas[tag]
                    sumOfCurrentIsland += 1
                    maxIsland = max(maxIsland, sumOfCurrentIsland)
        return maxIsland

    def largestIsland2(self, grid: List[List[int]]) -> int:
        if not any(grid):
            return 0
        maxIsland = 0
        islandTag = 2
        areas = {}
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    result = [0] # [currentArea]
                    self.dfs2(grid, row, col, islandTag, result)
                    areas[islandTag] = result[0]
                    maxIsland = max(maxIsland, result[0])
                    islandTag += 1
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    visited = set()
                    sumOfArea = 1
                    directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                    for row, col in directions:
                        if not self.isWater(grid, row, col):
                            visited.add(grid[row][col])
                    for tag in visited:
                        sumOfArea += areas[tag]
                    maxIsland = max(maxIsland, sumOfArea)
        return maxIsland
    
    
    def dfs2(self, grid, row, col, islandTag, result):
        if self.isWater(grid, row, col) or grid[row][col] != 1:
            return
        result[0] += 1
        grid[row][col] = islandTag
        directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for row, col in directions:
            self.dfs2(grid, row, col, islandTag, result)

    def dfs(self, grid, row, col, islandTag, size):
        if self.isWater(grid, row, col) or grid[row][col] != 1:
            return 0

        directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        grid[row][col] = islandTag
        for row, col in directions:
            size += self.dfs(grid, row, col, islandTag, 1)
        return size

    def isWater(self, grid, row, col):
        return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == 0


# Unit Tests
funcs = [Solution().largestIsland, Solution().largestIsland2]


class TestLargestIsland(unittest.TestCase):
    def testLargestIsland1(self):
        for func in funcs:
            grid = [[1,0],[0,1]]
            self.assertEqual(func(grid=grid), 3)

    def testLargestIsland2(self):
        for func in funcs:
            grid = [[1,1],[1,0]]
            self.assertEqual(func(grid=grid), 4)

    def testLargestIsland3(self):
        for func in funcs:
            grid = [[1,1],[1,1]]
            self.assertEqual(func(grid=grid), 4)

if __name__ == "__main__":
    unittest.main()
