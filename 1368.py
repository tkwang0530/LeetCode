"""
1368. Minimum Cost to Make at Least One Valid Path in a Grid
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
- 1 which means go to the cell to the right. (i.e. go from grid[i][j] to grid[i][j+1])
- 2 which means go to the cell to the left. (i.e. go from grid[i][j] to grid[i][j-1])
- 3 which means go to the cell to the lower cell. (i.e. from grid[i][j] to grid[i+1][j])
- 4 which means go to the cell to the upper cell. (i.e. from grid[i][j] to grid[i-1][j])

Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m-1, n-1) following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

Example1:
Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.

Example2:
Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).

Example3:
Input: grid = [[1,2],[4,3]]
Output: 1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 4
"""

"""
Note:
1. dijkstra: O(nlogn) time | O(n) space - where n is len(grid) * len(grid[0])
"""

import collections, heapq
from typing import List
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # 1:go right, 2:go left, 3:go down, 4:go up
        def getNextPosition(row, col, direction):
            if direction == 1:
                col += 1
            elif direction == 2:
                col -= 1
            elif direction == 3:
                row += 1
            else:
                row -= 1
            return row, col

        def isInGrid(row, col) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        height, width = len(grid), len(grid[0])
        table = collections.defaultdict(lambda: float('inf'))
        minHeap = [(0, 0, 0)]

        while minHeap:
            cost, row, col = heapq.heappop(minHeap)
            
            if row == height-1 and col == width-1:
                return cost
            
            if cost >= table[(row, col)]:
                continue
            else:
                table[(row, col)] = cost

            for direction in range(1, 4+1):
                nextRow, nextCol = getNextPosition(row, col, direction)
                if not isInGrid(nextRow, nextCol) or cost >= table[(nextRow, nextCol)]:
                    continue
                
                if direction == grid[row][col]:
                    heapq.heappush(minHeap, (cost, nextRow, nextCol))
                else:
                    heapq.heappush(minHeap, (cost+1, nextRow, nextCol))
        return -1


            

# Unit Tests
import unittest
funcs = [Solution().minCost]

class TestMinCost(unittest.TestCase):
    def testMinCost1(self):
        for func in funcs:
            grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
            self.assertEqual(func(grid=grid), 3)

    def testMinCost2(self):
        for func in funcs:
            grid = [[1,1,3],[3,2,2],[1,1,4]]
            self.assertEqual(func(grid=grid), 0)

    def testMinCost3(self):
        for func in funcs:
            grid = [[1,2],[4,3]]
            self.assertEqual(func(grid=grid), 1)


if __name__ == "__main__":
    unittest.main()
