"""
240. Search a 2D Matrix II
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
- Integers in each row are sorted in ascending from left to right
- Integers in each column are sorted in ascending from top to bottom.

Example1:
Input: matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
], target = 5
Output: true

Example2:
Input: matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
], target = 20
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9
"""

""" 
1. start from left bottom, go up or go right: O(n+m) time | O(1) space
where m is matrix.length and n is matrix[i].length
2. 1D binary Search with range check: O(mlogn) time | O(1) space
where m is matrix.length and n is matrix[i].length
"""

from typing import List
class Solution(object):
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startRow = len(matrix) - 1
        startCol = 0
        while startRow >= 0 and startCol <= len(matrix[0]) - 1:
            value = matrix[startRow][startCol]
            if value > target:
                startRow -= 1
            elif value < target:
                startCol += 1
            else:
                return True
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                left, right = 0, len(matrix[0]) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    value = row[mid]
                    if value < target:
                        left = mid + 1
                    elif value > target:
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
            matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
            target = 5
            self.assertEqual(func(matrix=matrix, target=target), True)

    def testSearchMatrix2(self):
        for func in funcs:
            matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
            target = 20
            self.assertEqual(func(matrix=matrix, target=target), False)

if __name__ == "__main__":
    unittest.main()
