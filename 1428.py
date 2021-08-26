"""
1428. Leftmost Column with at Least a One
(This problem is an interactive problem.)

A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:
- BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
- BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.

Example1:
Input: mat = [
    [0, 0],
    [1, 1]
]
Output: 0

Example2:
Input: mat = [
    [0, 0],
    [0, 1]
]
Output: 1

Example3:
Input: mat = [
    [0, 0],
    [0, 0]
]
Output: -1

Example4:
Input: mat = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]
Output: 1
"""

"""
Note:
1. track col and traverse from top-right to bottom-left: O(n+m)
(1) start from the top-right corner
(2) if we find 1, go left, otherwise go down
"""

from typing import List
import unittest
class BinaryMatrix:
    def __init__(self, mat: List[List[int]]):
        self.mat = mat
    
    def get(self, row, col):
        return self.mat[row][col]

    def dimensions(self):
        return [len(self.mat), len(self.mat[0])]

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        rows, cols = binaryMatrix.dimensions()
        row, col = 0, cols - 1
        leftMostCol = -1
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                leftMostCol = col
                col -= 1
            else:
                row += 1
        return leftMostCol



# Unit Tests
funcs = [Solution().leftMostColumnWithOne]


class TestLeftMostColumnWithOne(unittest.TestCase):
    def testLeftMostColumnWithOne1(self):
        for func in funcs:
            binaryMatrix = BinaryMatrix([[0, 0],[1, 1]])
            self.assertEqual(func(binaryMatrix=binaryMatrix), 0)

    def testLeftMostColumnWithOne2(self):
        for func in funcs:
            binaryMatrix = BinaryMatrix([[0, 0],[0, 1]])
            self.assertEqual(func(binaryMatrix=binaryMatrix), 1)

    def testLeftMostColumnWithOne3(self):
        for func in funcs:
            binaryMatrix = BinaryMatrix([[0, 0],[0, 0]])
            self.assertEqual(func(binaryMatrix=binaryMatrix), -1)

    def testLeftMostColumnWithOne4(self):
        for func in funcs:
            binaryMatrix = BinaryMatrix([[0, 0, 0, 1],[0, 0, 1, 1],[0, 1, 1, 1]])
            self.assertEqual(func(binaryMatrix=binaryMatrix), 1)

if __name__ == "__main__":
    unittest.main()
