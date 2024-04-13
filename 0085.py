"""
85. Maximal Rectangle
description: https://leetcode.com/problems/maximal-rectangle/description
"""

"""
Note:
1. monotonic stack + dp: O(mn) time | O(n) space - where m is the number of rows and n is the number of columns
"""

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            maxArea = 0
            stack = [] # [(index, height)]

            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i-index))
                    start = index
                stack.append((start, h))
            
            for i, h in stack:
                maxArea = max(maxArea, h * (len(heights) - i))

            return maxArea

        rows = len(matrix)
        cols = len(matrix[0])
        maxArea = 0
        for row in range(rows):
            # prepare histogram
            for col in range(cols):
                matrix[row][col] = int(matrix[row][col])
                if matrix[row][col] > 0 and row > 0:
                    matrix[row][col] += matrix[row-1][col]
            
            maxArea = max(maxArea, largestRectangleArea(matrix[row]))
        return maxArea

# Unit Tests
import unittest
funcs = [Solution().maximalRectangle]

class TestMaximalRectangle(unittest.TestCase):
    def testMaximalRectangle1(self):
        for func in funcs:
            matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
            self.assertEqual(func(matrix=matrix), 6)

    def testMaximalRectangle2(self):
        for func in funcs:
            matrix = [["0"]]
            self.assertEqual(func(matrix=matrix), 0)

    def testMaximalRectangle3(self):
        for func in funcs:
            matrix = [["1"]]
            self.assertEqual(func(matrix=matrix), 1)

if __name__ == "__main__":
    unittest.main()
