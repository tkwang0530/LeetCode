"""
1579. Remove Max Number of Edges to Keep Graph Fully Traversable
description: https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/
"""

"""
Note:
1. Minimum Spanning Tree + Two Union Finds: O(V+E) time | O(V+E) space
"""

import unittest
from typing import List
class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n+1)]
        self.ranks = [1 for _ in range(n+1)]

    def find(self, u):
        if u != self.parents[u]:
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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        aliceUF = UnionFind(n)
        bobUF = UnionFind(n)

        blueEdges = []
        redEdges = []
        greenEdges = []
        for tp, u, v in edges:
            if tp == 3:
                blueEdges.append((u, v))
            elif tp == 2:
                greenEdges.append((u, v))
            else:
                redEdges.append((u, v))

        blueUsed = redUsed = greenUsed = 0
        for u, v in blueEdges:
            blueUsed += aliceUF.union(u, v)
        
        bobUF.parents = aliceUF.parents.copy()
        bobUF.ranks = aliceUF.ranks.copy()

        for u, v in redEdges:
            redUsed += aliceUF.union(u, v)

        for u, v in greenEdges:
            greenUsed += bobUF.union(u, v)

        return len(edges)-(blueUsed+redUsed+greenUsed) if (blueUsed+redUsed==n-1) and (blueUsed+greenUsed==n-1) else -1
# Unit Tests
funcs = [Solution().maxNumEdgesToRemove]


class TestMaxNumEdgesToRemove(unittest.TestCase):
    def testMaxNumEdgesToRemove1(self):
        for maxNumEdgesToRemove in funcs:
            n = 4
            edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
            self.assertEqual(maxNumEdgesToRemove(n=n, edges=edges), 2)

    def testMaxNumEdgesToRemove2(self):
        for maxNumEdgesToRemove in funcs:
            n = 4
            edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
            self.assertEqual(maxNumEdgesToRemove(n=n, edges=edges), 0)

    def testMaxNumEdgesToRemove3(self):
        for maxNumEdgesToRemove in funcs:
            n = 4
            edges = [[3,2,3],[1,1,2],[2,3,4]]
            self.assertEqual(maxNumEdgesToRemove(n=n, edges=edges), -1)


if __name__ == "__main__":
    unittest.main()
