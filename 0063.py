"""
63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Example1:
Input: obstacleGrid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


Example2:
Input: obstacleGrid = [
    [0,1],
    [0,0]
]
Output: 1

Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""

"""
1. DP: O(mn) time | O(mn space)
dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
2. DP (in-place): O(mn) time | O(1)
3. DP (optimized): O(mn) time | O(n) space
"""

from typing import List
import unittest
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        dp = []
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        for row in range(rows):
            dp.append([0] * cols)
        
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1

        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    if row >= 1:
                        dp[row][col] += dp[row-1][col]
                    if col >= 1:
                        dp[row][col] += dp[row][col -1]
        return dp[-1][-1]

    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for row in range(1, rows):
            obstacleGrid[row][0] = obstacleGrid[row-1][0] * (1-obstacleGrid[row][0])
        
        for col in range(1, cols):
            obstacleGrid[0][col] = obstacleGrid[0][col-1] * (1-obstacleGrid[0][col])
        
        for row in range(1, rows):
            for col in range(1, cols):
                obstacleGrid[row][col] = (obstacleGrid[row-1][col] + obstacleGrid[row][col-1]) * (1-obstacleGrid[row][col])
        
        return obstacleGrid[-1][-1]

    def uniquePathsWithObstacles3(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[0] = 1 - obstacleGrid[0][0]
        if dp[0] == 0:
            return 0
        for col in range(1, cols):
            dp[col] = dp[col-1] * (1 - obstacleGrid[0][col])
        
        for row in range(1, rows):
            dp[0] *= (1 - obstacleGrid[row][0])
            for col in range(1, cols):
                dp[col] = (dp[col-1] + dp[col]) * (1 - obstacleGrid[row][col])
        return dp[-1]

# Unit Tests
funcs = [Solution().uniquePathsWithObstacles, Solution().uniquePathsWithObstacles2, Solution().uniquePathsWithObstacles3]


class TestUniquePathsWithObstacles(unittest.TestCase):
    def testUniquePathsWithObstacles1(self):
        for func in funcs:
            obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
            self.assertEqual(func(obstacleGrid=obstacleGrid), 2)

    def testUniquePathsWithObstacles2(self):
        for func in funcs:
            obstacleGrid = [[0,1],[0,0]]
            self.assertEqual(func(obstacleGrid=obstacleGrid), 1)

    def testUniquePathsWithObstacles3(self):
        for func in funcs:
            obstacleGrid = [[0,1]]
            self.assertEqual(func(obstacleGrid=obstacleGrid), 0)

    def testUniquePathsWithObstacles4(self):
        for func in funcs:
            obstacleGrid = [[0], [1]]
            self.assertEqual(func(obstacleGrid=obstacleGrid), 0)

if __name__ == "__main__":
    unittest.main()
