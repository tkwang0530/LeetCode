"""
1632. Rank Transform of a Matrix
description: https://leetcode.com/problems/rank-transform-of-a-matrix/description/
"""

"""
Note:
1. UnionFind + Sort + HashMap: O(mnlog(mn)) time | O(mn) space
"""

from typing import List
import collections
class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents
            [u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pv] < self.ranks[pu]:
            self.parents[pv] = pu
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1
        return True

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        maxRowRecord = {} # <row, (maxVal, rank)>
        maxColRecord = {} # <col, (maxVal, rank)>
        uf = UnionFind(rows * cols)
        rowValColumns = collections.defaultdict(list) # <(row,val): [col1, col2]>
        colValRows = collections.defaultdict(list) # <(col,val): [row1, row2]>

        def getIndex(r, c):
            return r * cols + c
        
        for row in range(rows):
            for col in range(cols):
                val = matrix[row][col]
                rowValColumns[(row,val)].append(col)
                colValRows[(col,val)].append(row)
        

        for row,val in rowValColumns.keys():
            col = rowValColumns[(row,val)][0]
            u = getIndex(row, col)
            for c in rowValColumns[(row,val)]:
                v = getIndex(row, c)
                uf.union(u, v)

        for col,val in colValRows.keys():
            row = colValRows[(col,val)][0]
            u = getIndex(row, col)
            for r in colValRows[(col,val)]:
                v = getIndex(r, col)
                uf.union(u, v)
        
        valParentGroup = collections.defaultdict(list) # <(val,parent): [(row1, col1), (row2, col2)]>
        for row in range(rows):
            for col in range(cols):
                val = matrix[row][col]
                parent = uf.find(getIndex(row, col))
                valParentGroup[(val, parent)].append((row, col))

        output = [[0] * cols for _ in range(rows)]
        for valParent in sorted(valParentGroup.keys()):
            val = valParent[0]
            group = valParentGroup[valParent]
            newRank = 1
            for r, c in group:
                if r in maxRowRecord:
                    if val >= maxRowRecord[r][0]:
                        newRank = max(newRank, maxRowRecord[r][1] + (val != maxRowRecord[r][0]))
                if c in maxColRecord:
                    if val >= maxColRecord[c][0]:
                        newRank = max(newRank, maxColRecord[c][1] + (val != maxColRecord[c][0]))

            for r, c in group:
                maxRowRecord[r] = (val, newRank)
                maxColRecord[c] = (val, newRank)
                output[r][c] = newRank
        return output

# Unit Tests
import unittest
funcs = [Solution().matrixRankTransform]
class TestMatrixRankTransform(unittest.TestCase):
    def testMatrixRankTransform1(self):
        for matrixRankTransform in funcs:
            matrix = [[1,2],[3,4]]
            self.assertEqual(matrixRankTransform(matrix=matrix), [[1,2],[2,3]])

    def testMatrixRankTransform2(self):
        for matrixRankTransform in funcs:
            matrix = [[7,7],[7,7]]
            self.assertEqual(matrixRankTransform(matrix=matrix), [[1,1],[1,1]])

    def testMatrixRankTransform3(self):
        for matrixRankTransform in funcs:
            matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
            self.assertEqual(matrixRankTransform(matrix=matrix), [[4,2,3],[1,3,4],[5,1,6],[1,3,4]])

if __name__ == "__main__":
    unittest.main()
