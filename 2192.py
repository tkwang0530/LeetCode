"""
2192. All Ancestors of a Node in a Directed Acyclic Graph
description: https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/
"""

"""
Note:
1. dfs + memo: O(V+E) time | O(V+E) space - where V is the number of vertices and E is the number of edges in the graph
"""

import unittest, collections
from typing import List
import functools
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        parents = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            parents[v].append(u)

        @functools.lru_cache(None)
        def dfs(node):
            ancestors = set()
            for parent in parents[node]:
                ancestors.add(parent)
                ancestors |= dfs(parent)
            return ancestors

        output = []
        for node in range(n):
            output.append(sorted(dfs(node)))
        return output

# Unit Tests
funcs = [Solution().getAncestors]


class TestGetAncestors(unittest.TestCase):
    def testGetAncestors1(self):
        for getAncestors in funcs:
            n = 8
            edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
            self.assertEqual(getAncestors(n=n, edges=edges), [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]])

    def testGetAncestors2(self):
        for getAncestors in funcs:
            n = 5
            edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
            self.assertEqual(getAncestors(n=n, edges=edges),[[],[0],[0,1],[0,1,2],[0,1,2,3]])

if __name__ == "__main__":
    unittest.main()
