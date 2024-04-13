"""
3108. Minimum Cost Walk in Weighted Graph
description: https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description/
"""

"""
Note:
1. UnionFind + HashTable: O(n+E+Q) time | O(n+Q+E) space - where e is the length of edges, q is the length of array query
"""

from typing import List
class UnionFind:
    def __init__(self, n: int):
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
    


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parentMinCost = {}
        uf = UnionFind(n)
        for u,v,_ in edges:
            uf.union(u, v)
        
        for u,_,w in edges:
            p = uf.find(u)
            if p not in parentMinCost:
                parentMinCost[p] = w
            else:
                parentMinCost[p] &= w
        
        output = [-1] * len(query)
        for i, (u, v) in enumerate(query):
            if uf.find(u) == uf.find(v):
                output[i] = parentMinCost[uf.find(u)]
        return output


# Unit Tests
import unittest
funcs = [Solution().minimumCost]

class TestMinimumCost(unittest.TestCase):
    def testMinimumCost1(self):
        for func in funcs:
            n = 5
            edges = [[0,1,7],[1,3,7],[1,2,1]]
            query = [[0,3],[3,4]]
            self.assertEqual(func(n=n, edges=edges, query=query), [1, -1])

    def testMinimumCost2(self):
        for func in funcs:
            n = 3
            edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
            query = [[1,2]]
            self.assertEqual(func(n=n, edges=edges, query=query), [0])

if __name__ == "__main__":
    unittest.main()
