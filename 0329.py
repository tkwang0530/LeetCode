"""
329. Longest Increasing Path in a Matrix
description: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
"""

"""
Note:
1. dfs+memo: O(mn) time | O(mn) space - where m is the number of rows and n is the number of columns in the matrix
"""

import collections, functools
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        @functools.lru_cache(None)
        def dfs(row, col) -> int:
            value = matrix[row][col]
            maxLen = 1
            for nextRow, nextCol in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if nextRow in (-1, rows) or nextCol in (-1, cols):
                    continue
                nextVal = matrix[nextRow][nextCol]
                if value < nextVal:
                    maxLen = max(maxLen, 1 + dfs(nextRow, nextCol))

            return maxLen
        
        maxLen = 0
        for row in range(rows):
            for col in range(cols):
                maxLen = max(maxLen, dfs(row, col))

        return maxLen

# Unit Tests
import unittest
funcs = [Solution().longestIncreasingPath]


class TestLongestIncreasingPath(unittest.TestCase):
    def testLongestIncreasingPath1(self):
        for func in funcs:
            matrix = [[9,9,4],[6,6,8],[2,1,1]]
            self.assertEqual(func(matrix=matrix), 4)

    def testLongestIncreasingPath2(self):
        for func in funcs:
            matrix = [[3,4,5],[3,2,6],[2,2,1]]
            self.assertEqual(func(matrix=matrix), 4)

    def testLongestIncreasingPath3(self):
        for func in funcs:
            matrix = [[1]]
            self.assertEqual(func(matrix=matrix), 1)

if __name__ == "__main__":
    unittest.main()
