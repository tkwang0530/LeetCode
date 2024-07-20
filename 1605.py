"""
1605. Find Valid Matrix Given Row and Column Sums
description: https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description
"""

"""
Note:
1. Greedy: O(nm + n+m) time | O(nm) space - where n is the length of rowSum and m is the length of colSum
"""




import unittest
from typing import List
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        grid = [[0] * cols for _ in range(rows)]
        row = col = 0
        while row < rows and col < cols:
            x = grid[row][col] = min(rowSum[row], colSum[col])
            rowSum[row] -= x
            colSum[col] -= x
            row += rowSum[row] == 0
            col += colSum[col] == 0

        return grid


# Unit Tests
funcs = [Solution().restoreMatrix]


class TestRestoreMatrix(unittest.TestCase):
    def testRestoreMatrix1(self):
        for func in funcs:
            rowSum = [3, 8]
            originalRowSum = rowSum[:]

            colSum = [4, 7]
            originalColSum = colSum[:]
            output = func(rowSum=rowSum, colSum=colSum)
            actualRowSum = [0] * len(rowSum)
            actualColSum = [0] * len(colSum)
            for row in range(len(rowSum)):
                for col in range(len(colSum)):
                    actualRowSum[row] += output[row][col]
                    actualColSum[col] += output[row][col]

            self.assertEqual(actualRowSum, originalRowSum)
            self.assertEqual(actualColSum, originalColSum)

    def testRestoreMatrix2(self):
        for func in funcs:
            rowSum = [5, 7, 10]
            originalRowSum = rowSum[:]

            colSum = [8, 6, 8]
            originalColSum = colSum[:]
            output = func(rowSum=rowSum, colSum=colSum)
            actualRowSum = [0] * len(rowSum)
            actualColSum = [0] * len(colSum)
            for row in range(len(rowSum)):
                for col in range(len(colSum)):
                    actualRowSum[row] += output[row][col]
                    actualColSum[col] += output[row][col]

            self.assertEqual(actualRowSum, originalRowSum)
            self.assertEqual(actualColSum, originalColSum)


if __name__ == "__main__":
    unittest.main()
