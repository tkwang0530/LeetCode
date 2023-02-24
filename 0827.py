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
1. Recursion (DFS) + HashTable: O(n^2) time | O(n^2) space
"""




from typing import List
import unittest
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0
        islandTag = 2
        islandTagAreas = {}  # <islandTag, area>
        rows = len(grid)
        cols = len(grid[0])

        def isWater(row, col):
            return row in (-1, rows) or col in (-1, cols) or grid[row][col] == 0

        def dfs(row, col, islandTag):
            if isWater(row, col) or grid[row][col] != 1:
                return 0
            grid[row][col] = islandTag
            area = 1
            directions = [(row-1, col), (row+1, col),
                          (row, col+1), (row, col-1)]
            for nextRow, nextCol in directions:
                area += dfs(nextRow, nextCol, islandTag)
            return area

        # First Round calculate each island's size and store them into areas
        # in the same time, mark every position of that island with same landTag
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row, col, islandTag)
                    maxIsland = max(maxIsland, area)
                    islandTagAreas[islandTag] = area
                    islandTag += 1

        # Second Round for each zero, check its neighbors' value, if the neighbor is not water,
        # add its islandTag into land map
        # than the sumOfArea = 1(self) + value(each islands'size) from the land map
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    landMap = {}
                    directions = [(row+1, col), (row-1, col),
                                  (row, col+1), (row, col-1)]
                    for nextRow, nextCol in directions:
                        if not isWater(nextRow, nextCol):
                            tag = grid[nextRow][nextCol]
                            landMap[tag] = islandTagAreas[tag]
                    maxIsland = max(maxIsland, 1 + sum(landMap.values()))

        return maxIsland


# Unit Tests
funcs = [Solution().largestIsland]


class TestLargestIsland(unittest.TestCase):
    def testLargestIsland1(self):
        for func in funcs:
            grid = [[1, 0], [0, 1]]
            self.assertEqual(func(grid=grid), 3)

    def testLargestIsland2(self):
        for func in funcs:
            grid = [[1, 1], [1, 0]]
            self.assertEqual(func(grid=grid), 4)

    def testLargestIsland3(self):
        for func in funcs:
            grid = [[1, 1], [1, 1]]
            self.assertEqual(func(grid=grid), 4)


if __name__ == "__main__":
    unittest.main()
