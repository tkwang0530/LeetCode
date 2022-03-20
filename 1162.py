"""
1162. As Far from Land as Possible
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Example1:
Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Example2:
Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""

"""
Notes:
1. BFS: O(n^2) time | O(n^2) space
"""

from typing import List
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        waters = set()
        candidates = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    candidates.add((row, col))
                else:
                    waters.add((row, col))
        
        if len(candidates) == 0 or len(waters) == 0:
            return -1
        
        steps = 0
        while waters:
            nextCandidates = set()
            for r, c in candidates:
                directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for nextR, nextC in directions:
                    if nextR < 0 or nextR >= rows or nextC < 0 or nextC >= cols:
                        continue
                    if grid[nextR][nextC] == 0 and (nextR, nextC) in waters:
                        waters.remove((nextR, nextC))
                        nextCandidates.add((nextR, nextC))
            steps += 1
            candidates = nextCandidates
        return steps


# Unit Tests
import unittest
funcs = [Solution().maxDistance]

class TestMaxDistance(unittest.TestCase):
    def testMaxDistance1(self):
        for func in funcs:
            grid = [[1,0,1],[0,0,0],[1,0,1]]
            self.assertEqual(func(grid=grid), 2)

    def testMaxDistance2(self):
        for func in funcs:
            grid = [[1,0,0],[0,0,0],[0,0,0]]
            self.assertEqual(func(grid=grid), 4)

if __name__ == "__main__":
    unittest.main()