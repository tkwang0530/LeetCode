"""
542. 01 Matrix
description: https://leetcode.com/problems/01-matrix/description/
"""

"""
Note:
1. BFS (layer order traversal): O(mn) time | O(mn) space - where m is the number of rows and n is the number of columns in the input matrix
"""

from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        currentNodes = []
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    currentNodes.append((row, col))
        
        output = [[0] * cols for _ in range(rows)]

        dist = 0
        while currentNodes:
            nextNodes = []
            for r, c in currentNodes:
                output[r][c] = dist
                for nextRow, nextCol in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if nextRow in (-1, rows) or nextCol in (-1, cols):
                        continue
                    
                    if mat[nextRow][nextCol] == 0:
                        continue

                    mat[nextRow][nextCol] = 0
                    nextNodes.append((nextRow, nextCol))
            
            currentNodes = nextNodes
            dist += 1
        return output

# Unit Tests
import unittest
funcs = [Solution().updateMatrix]

class TestUpdateMatrix(unittest.TestCase):
    def testUpdateMatrix1(self):
        for func in funcs:
            mat = [[0,0,0],[0,1,0],[0,0,0]]
            self.assertEqual(func(mat), [[0,0,0],[0,1,0],[0,0,0]])

    def testUpdateMatrix2(self):
        for func in funcs:
            mat = [[0,0,0],[0,1,0],[1,1,1]]
            self.assertEqual(func(mat), [[0,0,0],[0,1,0],[1,2,1]])

if __name__ == "__main__":
    unittest.main()