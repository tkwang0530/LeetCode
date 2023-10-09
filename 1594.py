"""
1594. Maximum Non Negative Product in a Matrix
description: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description/
"""

"""
Note:
1. dp: O(mn) time | O(mn) space - where m is len(grid) and n is len(grid[0])
"""

from typing import List
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        rows = len(grid)
        cols = len(grid[0])
        dp = [[(0,0)]*cols for _ in range(rows)]
        
        dp[0][0] = [grid[0][0], grid[0][0]]
        for col in range(1, cols):
            row = 0
            currentVal = grid[row][col]
            dp[row][col] = (currentVal * dp[row][col-1][0], currentVal * dp[row][col-1][1])
        
        for row in range(1, rows):
            col = 0
            currentVal = grid[row][col]
            dp[row][col] = (currentVal * dp[row-1][col][0], currentVal * dp[row-1][col][1])
        
        for row in range(1, rows):
            for col in range(1, cols):
                currentVal = grid[row][col]
                maxVal = float("-inf")
                minVal = float("inf")
                for val in dp[row-1][col]+dp[row][col-1]:
                    maxVal = max(maxVal, currentVal * val)
                    minVal = min(minVal, currentVal * val)
                dp[row][col] = (minVal, maxVal)
        
        return -1 if max(dp[-1][-1]) < 0 else max(dp[-1][-1]) % mod


# Unit Tests
import unittest
funcs = [Solution().maxProductPath]

class TestMaxProductPath(unittest.TestCase):
    def testMaxProductPath1(self):
        for func in funcs:
            grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
            self.assertEqual(func(grid=grid), -1)

    def testMaxProductPath2(self):
        for func in funcs:
            grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
            self.assertEqual(func(grid=grid), 8)

    def testMaxProductPath3(self):
        for func in funcs:
            grid = [[1,3],[0,-4]]
            self.assertEqual(func(grid=grid), 0)

if __name__ == "__main__":
    unittest.main()