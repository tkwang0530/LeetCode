"""
1727. Largest Submatrix With Rearrangements
You are given a binary matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

Example1:
Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.

Example2:
Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.

Example3:
Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m * n <= 10^5
matrix[i][j] is either 0 or 1.
"""

"""
Note:
1. PreSum + Sort: O(m*nlogn) time | O(n) space - where m is len(matrix) and n is len(matrix[0])
"""

from typing import List
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        cols = len(matrix[0])
        rows = len(matrix)
        heights = matrix[0]
        largestArea = sum(matrix[0])
        for row in range(1, rows):
            for col in range(cols):
                heights[col] = heights[col] + 1 if matrix[row][col] == 1 else 0
            
            for col, height in enumerate(sorted(heights, reverse=True)):
                largestArea = max(largestArea, (col+1) * height)
        return largestArea

# Unit Tests
import unittest
funcs = [Solution().largestSubmatrix]
class TestLargestSubmatrix(unittest.TestCase):
    def testLargestSubmatrix1(self):
        for func in funcs:
            matrix = [[0,0,1],[1,1,1],[1,0,1]]
            self.assertEqual(func(matrix=matrix), 4)

    def testLargestSubmatrix2(self):
        for func in funcs:
            matrix = [[1,0,1,0,1]]
            self.assertEqual(func(matrix=matrix), 3)

    def testLargestSubmatrix3(self):
        for func in funcs:
            matrix = [[1,1,0],[1,0,1]]
            self.assertEqual(func(matrix=matrix), 2)


if __name__ == "__main__":
    unittest.main()
