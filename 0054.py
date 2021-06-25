"""
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.


Example1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Example2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
"""

"""
Note:
1. Iterative Solution: O(n) time | O(n) space
2. Recursion Solution: O(n) time | O(n) space
"""




import unittest
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        startRow, endRow = 0, len(matrix) - 1
        startCol, endCol = 0, len(matrix[0]) - 1
        while startRow <= endRow and startCol <= endCol:
            for col in range(startCol, endCol + 1):
                result.append(matrix[startRow][col])
            if startRow == endRow:
                break
            for row in range(startRow + 1, endRow + 1):
                result.append(matrix[row][endCol])
            if startCol == endCol:
                break
            for col in reversed(range(startCol, endCol)):
                result.append(matrix[endRow][col])
            if startRow == endRow:
                break
            for row in reversed(range(startRow+1, endRow)):
                result.append(matrix[row][startCol])
            startCol += 1
            endCol -= 1
            startRow += 1
            endRow -= 1
        return result

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        result = []
        self.spiralFill(matrix, 0, len(matrix) - 1,
                        0, len(matrix[0]) - 1, result)
        return result

    def spiralFill(self, matrix: List[List[int]], startRow: int, endRow: int, startCol: int, endCol: int, result: List[int]) -> None:
        if startRow > endRow or startCol > endCol:
            return
        for col in range(startCol, endCol + 1):
            result.append(matrix[startRow][col])
        if startRow == endRow:
            return
        for row in range(startRow + 1, endRow+1):
            result.append(matrix[row][endCol])
        if startCol == endCol:
            return
        for col in reversed(range(startCol, endCol)):
            result.append(matrix[endRow][col])
        if startRow == endRow:
            return
        for row in reversed(range(startRow+1, endRow)):
            result.append(matrix[row][startCol])
        return self.spiralFill(matrix, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)


# Unit Tests
funcs = [Solution().spiralOrder, Solution().spiralOrder2]


class TestSpiralOrder(unittest.TestCase):
    def testSpiralOrder1(self):
        for func in funcs:
            matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            self.assertEqual(
                func(matrix=matrix),
                [1, 2, 3, 6, 9, 8, 7, 4, 5]
            )

    def testSpiralOrder2(self):
        for func in funcs:
            matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
            self.assertEqual(
                func(matrix=matrix),
                [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
            )


if __name__ == "__main__":
    unittest.main()
