"""
323. Number of Connected Components in an Undirected Graph
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example1:
Input: n = 5, and edges = [[0, 1], [1, 2], [3, 4]]
Output: 2
"""

"""
Note:
1. DFS: O(V+E) time | O(V+E) space
do a dfs/bfs and put all visited nodes into a set.
count how many dfs/bfs we have to do to visit all nodes.
"""




import unittest
import collections
from typing import List
class Solution(object):
    def countComponents(self, n: int, edges: List[List[int]]) -> int:  # dfs
        hmap = collections.defaultdict(list)  # adj. list
        for u, v in edges:
            hmap[u].append(v)
            hmap[v].append(u)
        count = 0
        visited = set()

        for node in range(n):
            if node not in visited:
                self.dfs(node, visited, hmap)
                count += 1
        return count

    def dfs(self, node, visited, hmap):
        if node in hmap:  # if node has no edges, it won't be in hmap
            for neighbor in hmap[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    self.dfs(neighbor, visited, hmap)


    # Unit Tests
funcs = [Solution().countComponents]


class TestCountComponents(unittest.TestCase):
    def testCountComponents1(self):
        for func in funcs:
            n = 5
            edges = [[0, 1], [1, 2], [3, 4]]
            self.assertEqual(
                func(n=n, edges=edges), 2)


if __name__ == "__main__":
    unittest.main()
