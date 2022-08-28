"""
1329. Sort the Matrix Diagonally
A matrix diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Example1:
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Example2:
Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""

"""
Note:
1. Sort: O((m+n)log(m+n)) time | O(m+n) space - where m is the number of rows and n is the number of columns
"""

from typing import List
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        startingPoints = []
        rows = len(mat)
        cols = len(mat[0])
        for row in range(1, rows):
            startingPoints.append((row, 0))
        
        for col in range(cols):
            startingPoints.append((0, col))
            
        for startRow, startCol in startingPoints:
            nums = []
            row, col = startRow, startCol
            while row < rows and col < cols:
                nums.append(mat[row][col])
                row += 1
                col += 1
            
            nums.sort()
            row, col = startRow, startCol
            for num in nums:
                mat[row][col] = num
                row += 1
                col += 1
        return mat

# Unit Tests
import unittest
funcs = [Solution().diagonalSort]
class TestDiagonalSort(unittest.TestCase):
    def testDiagonalSort1(self):
        for func in funcs:
            mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
            self.assertEqual(func(mat=mat), [[1,1,1,1],[1,2,2,2],[1,2,3,3]])

    def testDiagonalSort2(self):
        for func in funcs:
            mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
            self.assertEqual(func(mat=mat), [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]])

if __name__ == "__main__":
    unittest.main()
