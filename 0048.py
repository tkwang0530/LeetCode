"""
48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example1:
Input: matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
Output: [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]

Example2:
Input: matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]
Output: [
    [15,13,2,5],
    [14,3,4,1],
    [12,6,8,9],
    [16,7,10,11]
]

Example3:
Input: matrix = [[1]]
Output: [[1]]

Example4:
Input: matrix = [
    [1,2],
    [3,4]
]
Output: [
    [3,1],
    [4,2]
]

Constraints:
matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

"""
Note:
1. Transpose and then reverse each row
matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if the problem change to anti-clockwise => transpose and then reverse each col
"""

from typing import List
import unittest
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(len(matrix)):
            matrix[i].reverse()


# Unit Tests
funcs = [Solution().rotate]


class TestRotate(unittest.TestCase):
    def testRotate1(self):
        for func in funcs:
            matrix = [[1,2,3],[4,5,6],[7,8,9]]
            func(matrix=matrix)
            self.assertEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])

    def testRotate2(self):
        for func in funcs:
            matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
            func(matrix=matrix)
            self.assertEqual(matrix, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

    def testRotate3(self):
        for func in funcs:
            matrix = [[1]]
            func(matrix=matrix)
            self.assertEqual(matrix, [[1]])

    def testRotate4(self):
        for func in funcs:
            matrix = [[1,2],[3,4]]
            func(matrix=matrix)
            self.assertEqual(matrix, [[3,1],[4,2]])

if __name__ == "__main__":
    unittest.main()