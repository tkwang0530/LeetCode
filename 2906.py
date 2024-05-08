"""
2906. Construct Product Matrix
description: https://leetcode.com/problems/construct-product-matrix/description/
"""

"""
Note:
1. PreSum: O(mn) time | O(mn) space - where m is len(grid) and n is len(grid[0])
"""

from itertools import product
from typing import List
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        M = 12345
        n = rows * cols

        prefixProducts = [1] * (rows*cols+1)
        suffixProducts = [1] * (rows*cols+1)

        def getPos(idx):
            return idx // cols, idx % cols

        def getIdx(row, col):
            return row * cols + col

        for i in range(1, n+1):
            row, col = getPos(i-1)
            prefixProducts[i] = (prefixProducts[i-1]*grid[row][col]) % M

        for i in range(n-2, -1, -1):
            row, col = getPos(i+1)
            suffixProducts[i] = (suffixProducts[i+1]*grid[row][col]) % M

        for row,col in product(range(rows), range(cols)):
            idx = getIdx(row, col)
            grid[row][col] = (prefixProducts[idx] * suffixProducts[idx]) % M
        return grid

# Unit Tests
import unittest
funcs = [Solution().constructProductMatrix]

class TestConstructProductMatrix(unittest.TestCase):
    def testConstructProductMatrix1(self):
        for constructProductMatrix in funcs:
            grid = [[1,2],[3,4]]
            self.assertEqual(constructProductMatrix(grid=grid), [[24,12],[8,6]])

    def testConstructProductMatrix2(self):
        for constructProductMatrix in funcs:
            grid = [[12345],[2],[1]]
            self.assertEqual(constructProductMatrix(grid=grid), [[2],[0],[0]])

if __name__ == "__main__":
    unittest.main()