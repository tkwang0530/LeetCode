"""
566. Reshape the Matrix
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
"""

"""
Note:
1. Brute-Force: O(mn) time | O(mn) space - where m, n is the dimension of the given matrix mat
"""




import unittest
from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if rows * cols != r * c:
            return mat
        reshapedMat = [[0] * c for _ in range(r)]
        for row in range(rows):
            for col in range(cols):
                idx = row * cols + col
                reshapedMat[idx // c][idx % c] = mat[row][col]
        return reshapedMat


# Unit Tests
funcs = [Solution().matrixReshape]


class TestMatrixReshape(unittest.TestCase):
    def testMatrixReshape1(self):
        for func in funcs:
            mat = [[1, 2], [3, 4]]
            r = 1
            c = 4
            self.assertEqual(func(mat=mat, r=r, c=c), [[1, 2, 3, 4]])

    def testMatrixReshape2(self):
        for func in funcs:
            mat = [[1, 2], [3, 4]]
            r = 2
            c = 4
            self.assertEqual(func(mat=mat, r=r, c=c), [[1, 2], [3, 4]])


if __name__ == "__main__":
    unittest.main()
