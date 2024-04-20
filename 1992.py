"""
1992. Find All Groups of Farmland
description: https://leetcode.com/problems/find-all-groups-of-farmland/description/
"""

"""
Note:
1. UnionFind + HashMap: O(mn) space | O(mn) time - where m is the number of rows and n is the number of columns
"""

from typing import List
import collections
class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

    def find(self, u: int) -> int:
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u: int, v: int) -> bool:
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
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows = len(land)
        cols = len(land[0])
        def getIdx(row, col):
            return row * cols + col

        def getPos(idx):
            return (idx // cols,idx % cols)
        uf = UnionFind(rows * cols)
        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 0:
                    continue

                u = getIdx(row, col)
                if row < rows-1 and land[row+1][col] == 1:
                    v = getIdx(row+1, col)
                    uf.union(u, v)
                if col < cols-1 and land[row][col+1] == 1:
                    v = getIdx(row, col+1)
                    uf.union(u, v)
        
        parentsMin = collections.defaultdict(lambda: float("inf"))
        parentsMax = collections.defaultdict(lambda: -float("inf"))
        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 0:
                    continue
                u = getIdx(row, col)
                p = uf.find(u)
                parentsMin[p] = min(parentsMin[p], u)
                parentsMax[p] = max(parentsMax[p], u)

        output = []
        for p, minIdx in parentsMin.items():
            maxIdx = parentsMax[p]
            r1, c1 = getPos(minIdx)
            r2, c2 = getPos(maxIdx)
            output.append([r1, c1, r2, c2])
        return output

# Unit Tests
import unittest
funcs = [Solution().findFarmland]

class TestFindFarmland(unittest.TestCase):
    def testFindFarmland1(self):
        for func in funcs:
            land = [[1,0,0],[0,1,1],[0,1,1]]
            self.assertEqual(func(land=land), [[0,0,0,0],[1,1,2,2]])

    def testFindFarmland2(self):
        for func in funcs:
            land = [[1,1],[1,1]]
            self.assertEqual(func(land=land), [[0,0,1,1]])

if __name__ == "__main__":
    unittest.main()
