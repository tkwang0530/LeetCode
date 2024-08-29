"""
947. Most Stones Removed with Same Row or Column
description: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
"""

"""
Note:
1. Union Find: O(n^2) time | O(n) space - where n is the number of stones
"""


from typing import List
import unittest, collections

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
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
    def removeStones(self, stones: List[List[int]]) -> int:
        rowCols = collections.defaultdict(set)
        colRows = collections.defaultdict(set)

        for i, (row, col) in enumerate(stones):
            rowCols[row].add(i)
            colRows[col].add(i)

        uf = UnionFind(len(stones))
        unions = 0
        for u, (row, col) in enumerate(stones):
            # same row
            for v in rowCols[row]:
                unions += uf.union(u, v)

            # same col
            for v in colRows[col]:
                unions += uf.union(u, v)

        return unions


# Unit Tests
funcs = [Solution().removeStones]

class TestRemoveStones(unittest.TestCase):
    def testRemoveStones1(self):
        for func in funcs:
            stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
            self.assertEqual(func(stones=stones), 5)

    def testRemoveStones2(self):
        for func in funcs:
            stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
            self.assertEqual(func(stones=stones), 3)

    def testRemoveStones3(self):
        for func in funcs:
            stones = [[0,0]]
            self.assertEqual(func(stones=stones), 0)


if __name__ == "__main__":
    unittest.main()
