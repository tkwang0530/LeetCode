"""
221. Maximal Square
description: https://leetcode.com/problems/maximal-square/description/
"""

"""
Note:
1. dp: O(mn) time | O(1) space
2. dp (1D): O(mn) time | O(n) space
"""

import unittest, collections
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        maxArea = 0
        for row in range(rows):
            for col in range(cols):
                dpLeft = matrix[row][col-1] if col-1 >= 0 else 0
                dpTop = matrix[row-1][col] if row-1 >= 0 else 0
                dpTopLeft = matrix[row-1][col-1] if (row-1 >= 0 and col-1 >= 0) else 0
                if matrix[row][col] == "1":
                    matrix[row][col] = min(dpLeft, dpTop, dpTopLeft) + 1
                else:
                    matrix[row][col] = 0
                maxArea = max(maxArea, matrix[row][col] ** 2)
        return maxArea

class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = collections.defaultdict(int)

        maxArea = 0
        for row in range(rows):
            dp1 = collections.defaultdict(int)
            for col in range(cols):
                if matrix[row][col] == "1":
                    dp1[col] = 1 + min(
                        dp[col],
                        dp[col-1],
                        dp1[col-1]
                    )
                    maxArea = max(maxArea, dp1[col] ** 2)
            dp = dp1

        return maxArea

# Unit Tests
import unittest
funcs = [Solution().maximalSquare, Solution2().maximalSquare]
class TestMaximalSquare(unittest.TestCase):
    def testMaximalSquare1(self):
        for func in funcs:
            matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
            self.assertEqual(func(matrix=matrix), 4)

    def testMaximalSquare2(self):
        for func in funcs:
            matrix = [["0","1"],["1","0"]]
            self.assertEqual(func(matrix=matrix), 1)

    def testMaximalSquare3(self):
        for func in funcs:
            matrix = [["0"]]
            self.assertEqual(func(matrix=matrix), 0)

if __name__ == "__main__":
    unittest.main()
