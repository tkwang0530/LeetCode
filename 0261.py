"""
261. Graph Valid Tree
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example1:
Input: n = 5, and edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true

Example2:
Input: n = 5, and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

"""
Note:
1. DFS: O(V+E) time | O(V+E) space
no need to detect cycle (although detecting cycle can return early)
we just need to check
(1) number of edges = number of nodes - 1
(2) graph is connected (after 1 traversal, all nodes are visited)
"""




import unittest
import collections
from typing import List
class Solution(object):
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        hmap = collections.defaultdict(list)  # adj. list
        for u, v in edges:  # edge = [0, 1]
            hmap[u].append(v)  # u -> v
            hmap[v].append(u)  # v -> u
        visited = [False] * n
        self.dfs(0, hmap, visited)
        return False not in visited  # check graph is connected

    def dfs(self, curr, hmap, visited):
        if visited[curr]:
            return
        visited[curr] = True
        for neighbor in hmap[curr]:
            self.dfs(neighbor, hmap, visited)


    # Unit Tests
funcs = [Solution().validTree]


class TestValidTree(unittest.TestCase):
    def testValidTree1(self):
        for func in funcs:
            n = 5
            edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
            self.assertEqual(
                func(n=n, edges=edges), True)

    def testValidTree2(self):
        for func in funcs:
            n = 5
            edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
            self.assertEqual(
                func(n=n, edges=edges), False)


if __name__ == "__main__":
    unittest.main()
