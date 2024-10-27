"""
1277. Count Square Submatrices with All Ones
description: https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
"""

"""
Note:
1. dfs+memo: O(mn) time | O(mn) space - where m and n are the dimension of the matrix
2. dp (2D): O(mn) time | O(mn) space - where m and n are the dimension of the matrix
3. dp (1D): O(mn) time | O(n) space - where m and n are the dimension of the matrix
ref: https://www.youtube.com/watch?v=5Li-cR5h_uw
"""

import functools, collections
from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        @functools.lru_cache(None) 
        def dfs(row, col):
            if row == rows or col == cols or not matrix[row][col]:
                return 0

            return 1+ min(dfs(row+1, col), dfs(row, col+1), dfs(row+1, col+1))

        output = 0
        for row in range(rows):
            for col in range(cols):
                output += dfs(row, col)

        return output

class Solution2:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = collections.defaultdict(int)
        output = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]:
                    dp[(row, col)] = 1 + min(
                        dp[(row-1, col)],
                        dp[(row, col-1)],
                        dp[(row-1, col-1)]
                    )
                    output += dp[(row, col)]

        return output

class Solution3:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = collections.defaultdict(int)
        output = 0
        for row in range(rows):
            dp1 = collections.defaultdict(int)
            for col in range(cols):
                if matrix[row][col]:
                    dp1[col] = 1 + min(
                        dp[col],
                        dp1[col-1],
                        dp[col-1]
                    )
                    output += dp1[col]
            dp = dp1

        return output

funcs = [Solution().countSquares, Solution2().countSquares, Solution3().countSquares]

import unittest
class TestCountSquares(unittest.TestCase):
    def testCountSquares1(self):
        for func in funcs:
            matrix = [
                       [0,1,1,1],
                       [1,1,1,1],
                       [0,1,1,1]
                     ]
            self.assertEqual(func(matrix=matrix), 15)

    def testCountSquares2(self):
        for func in funcs:
            matrix = [
                       [1,0,1],
                       [1,1,0],
                       [1,1,0]
                     ]
            self.assertEqual(func(matrix=matrix), 7)

if __name__ == "__main__":
    unittest.main()
