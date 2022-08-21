"""
2017. Grid Game
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ( (r, c) to (r, c + 1) ) or down ( (r, c) to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1) collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of it collects. If both rebots play optimally, return the number of points collected by the second robot.

Example1:
Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.

Example2:
Input: grid = [[3,3,1],[8,5,2]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 3 + 1 + 0 = 4 points.

Example3:
Input: grid = [[1,3,1,15],[1,3,3,1]]
Output: 7
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.

Constraints:
grid.length == 2
n == grid[r].length
1 <= n <= 5 * 10^4
1 <= grid[r][c] <= 10^5
"""

"""
Note:
1. PreSum: O(n) time | O(1) space
"""

from typing import List
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        for i in range(n-2, -1, -1):
            grid[1][i] = grid[1][i] + grid[1][i+1]
            grid[0][i] = grid[0][i] + grid[0][i+1]
        
        minScore = float("inf")
        for i in range(n):
            minScore = min(
                minScore,
                max(
                    grid[0][i+1] if i+1 < n else 0,
                    grid[1][0] - grid[1][i]
                )
            )
        return minScore

# Unit Tests
import unittest
funcs = [Solution().gridGame]
class TestGridGame(unittest.TestCase):
    def testGridGame1(self):
        for func in funcs:
            grid = [[2,5,4],[1,5,1]]
            self.assertEqual(func(grid=grid), 4)

    def testGridGame2(self):
        for func in funcs:
            grid = [[3,3,1],[8,5,2]]
            self.assertEqual(func(grid=grid), 4)

    def testGridGame3(self):
        for func in funcs:
            grid = [[1,3,1,15],[1,3,3,1]]
            self.assertEqual(func(grid=grid), 7)

if __name__ == "__main__":
    unittest.main()
