"""
1975. Maximum Matrix Sum
description: https://leetcode.com/problems/maximum-matrix-sum/description/
"""

"""
Note:
1. Greedy: O(mn) time | O(1) space - where m,n are the matrix's dimensions 
"""

from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negs = 0
        minAbs = float("inf")
        totalAbs = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                negs += matrix[row][col] < 0
                minAbs = min(minAbs, abs(matrix[row][col]))
                totalAbs += abs(matrix[row][col])

        return totalAbs - 2 * minAbs * (negs % 2)

import unittest
funcs = [Solution().maxMatrixSum]

class TestMaxMatrixSum(unittest.TestCase):
    def testMaxMatrixSum1(self):
        for func in funcs:
            matrix = [[1,-1],[-1,1]]
            self.assertEqual(func(matrix=matrix), 4)

    def testMaxMatrixSum2(self):
        for func in funcs:
            matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
            self.assertEqual(func(matrix=matrix), 16) 

if __name__ == "__main__":
    unittest.main()
