"""
304. Range Sum Query 2D - Immutable
Given a 2D matrix, handle multiple queries of the following type:
- Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:
- NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
- int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example1:
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m,n <= 200
-10^5 <= matrix[i][j] <= 10^5
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 10^4 calls will be made to sumRegion.
"""

"""
Note:
1. PreSum
__init__: O(mn) time | O(mn) space
sumRegion: O(1) time | O(1) space
where m is number of rows in matrix, and n is the number of columns in matrix
"""

from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.preSums = [[0] * (n+1) for _ in range(m+1)] # preSums[i][j] is the sum of all elements inside the rectangle [0,0,i-1, j-1]
        for row in range(1, m+1):
            for col in range(1, n+1):
                # sumRange(0, 0, r, c) = sumRange(0, 0, r-1, c) + sumRange(0, 0, r, c-1) - sumRange(0, 0, r-1, c-1) + matrix[r][c]
                self.preSums[row][col] = self.preSums[row-1][col] + self.preSums[row][col-1] - self.preSums[row-1][col-1] + matrix[row-1][col-1]

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        # sumRange(r1, c1, r2, c2) = sum[r2][c2] - sum[r2][c1-1] - sum[r1-1][c2] + sum[r1-1][c1-1]
        return self.preSums[r2+1][c2+1] - self.preSums[r2+1][c1] - self.preSums[r1][c2+1] + self.preSums[r1][c1]

# Unit Tests
import unittest
classes = [NumMatrix]
class TestNumMatrix(unittest.TestCase):

    def testNumMatrix1(self):
        matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
        for myclass in classes:
            numMatrix = myclass(matrix=matrix)
            self.assertEqual(numMatrix.sumRegion(2,1,4,3), 8)
            self.assertEqual(numMatrix.sumRegion(1,1,2,2), 11)
            self.assertEqual(numMatrix.sumRegion(1,2,2,4), 12)



if __name__ == "__main__":
    unittest.main()
