"""
74. Search a 2D Matrix
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Example1:
Input: matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
], target = 3
Output: true

Example2:
Input: matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""

""" 
1. Binary Search row and then col: O(logm + logn) time | O(1) space
2. Treat it as a sorted list: O(log(nm)) time | O(1) space
(1) n*m matrix convert to an array => matrix[x][y] => a[x*m + y]
(2) an array convert to n*m matrix => a[x] => matrix[x/m][x%m]
Note that the multiplication of n and m may cause overflow
"""

from typing import List
class Solution(object):
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        startRow, endRow = 0, rows - 1
        while startRow <= endRow:
            midRow = startRow + (endRow - startRow) // 2
            if target > matrix[midRow][-1]:
                startRow = midRow + 1
            elif target < matrix[midRow][0]:
                endRow = midRow - 1
            else:
                left, right = 0, cols - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    value = matrix[midRow][mid]
                    if target > value:
                        left = mid + 1
                    elif target < value:
                        right = mid - 1
                    else:
                        return True
                break
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target > matrix[mid // cols][mid % cols]:
                left = mid + 1
            elif target < matrix[mid // cols][mid % cols]:
                right = mid - 1
            else:
                return True
        return False

# Unit Tests
import unittest
funcs = [Solution().searchMatrix, Solution().searchMatrix2]

class TestSearchMatrix(unittest.TestCase):
    def testSearchMatrix1(self):
        for func in funcs:
            matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
            target = 3
            self.assertEqual(func(matrix=matrix, target=target), True)

    def testSearchMatrix2(self):
        for func in funcs:
            matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
            target = 13
            self.assertEqual(func(matrix=matrix, target=target), False)

    def testSearchMatrix3(self):
        for func in funcs:
            matrix = [[1,1]]
            target = 2
            self.assertEqual(func(matrix=matrix, target=target), False)

if __name__ == "__main__":
    unittest.main()
