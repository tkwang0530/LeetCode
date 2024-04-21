"""
1971. Find if Path Exists in Graph
description: https://leetcode.com/problems/find-if-path-exists-in-graph/description
"""

"""
Note:
1. UnionFind: O(n+e) time | O(n) space - where e is the number of edges
"""

from typing import List
class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

    def find(self, u) -> int:
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v) -> bool:
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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)

        return uf.find(source) == uf.find(destination)

# Unit Tests
import unittest
funcs = [Solution().validPath]

class TestValidPath(unittest.TestCase):
    def testValidPath1(self):
        for func in funcs:
            n = 3
            edges = [[0,1],[1,2],[2,0]]
            source = 0
            destination = 2
            self.assertEqual(func(n=n, edges=edges, source=source, destination=destination), True)

    def testValidPath2(self):
        for func in funcs:
            n = 6
            edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
            source = 0
            destination = 5
            self.assertEqual(func(n=n, edges=edges, source=source, destination=destination), False)

if __name__ == "__main__":
    unittest.main()
