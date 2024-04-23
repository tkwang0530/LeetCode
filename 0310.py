"""
310. Minimum Height Trees
description: https://leetcode.com/problems/minimum-height-trees/description/
"""

"""
Note:
1. BFS (layer order traversal + topological sort): O(n+e) time | O(n+e) space - where e is the number of edges
ref: https://leetcode.com/problems/minimum-height-trees/solutions/76055/share-some-thoughts
"""

import collections
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [i for i in range(n) if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                del graph[leaf]
                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves
        return leaves

# Unit Tests
import unittest
funcs = [Solution().findMinHeightTrees]

class TestFindMinHeightTrees(unittest.TestCase):
    def testFindMinHeightTrees1(self):
        for func in funcs:
            n = 4
            edges = [[1,0],[1,2],[1,3]]
            self.assertEqual(func(n=n, edges=edges), [1])

    def testFindMinHeightTrees2(self):
        for func in funcs:
            n = 6
            edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
            self.assertEqual(func(n=n, edges=edges), [3, 4])

if __name__ == "__main__":
    unittest.main()