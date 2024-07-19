"""
1380. Lucky Numbers in a Matrix
description: https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
"""

"""
Note:
1. Two Pass: O(m*n) time | O(m+n) space - where m is the number of rows, n is the number of columns
"""

from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        colMaxs = [-float("inf")] * cols
        rowMins = [float("inf")] * rows

        for row in range(rows):
            for col in range(cols):
                num = matrix[row][col]
                colMaxs[col] = max(colMaxs[col], num)
                rowMins[row] = min(rowMins[row], num)
        
        lucky = []
        for row in range(rows):
            for col in range(cols):
                num = matrix[row][col]
                if num == colMaxs[col] and num == rowMins[row]:
                    lucky.append(num)
                    break

        return lucky

# Unit Tests
import unittest
funcs = [Solution().luckyNumbers]
class TestLuckyNumbers(unittest.TestCase):
    def testLuckyNumbers1(self):
        for func in funcs:
            matrix = [[3,7,8],[9,11,13],[15,16,17]]
            self.assertEqual(func(matrix), [15])

    def testLuckyNumbers2(self):
        for func in funcs:
            matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
            self.assertEqual(func(matrix), [12])

    def testLuckyNumbers3(self):
        for func in funcs:
            matrix = [[7,8],[1,2]]
            self.assertEqual(func(matrix), [7])

if __name__ == "__main__":
    unittest.main()
