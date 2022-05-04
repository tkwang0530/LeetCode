"""
867. Transpose Matrix
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
-10^9 <= matrix[i][j] <= 10^9
"""

"""
Note:
1. brute-force: O(mn) time | O(1) space - where m is len(matrix) and n is len(matrix[i])
"""

from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        newMatrix = [[0] * m for _ in range(n)]
        for row in range(m):
            for col in range(n):
                newMatrix[col][row] = matrix[row][col]
        return newMatrix

# Unit Tests
import unittest
funcs = [Solution().transpose]

class TestTranspose(unittest.TestCase):
    def testTranspose1(self):
        for func in funcs:
            matrix = [[1,2,3],[4,5,6],[7,8,9]]
            self.assertEqual(func(matrix=matrix), [[1,4,7],[2,5,8],[3,6,9]])

    def testTranspose2(self):
        for func in funcs:
            matrix = [[1,2,3],[4,5,6]]
            self.assertEqual(func(matrix=matrix), [[1,4],[2,5],[3,6]])

if __name__ == "__main__":
    unittest.main()