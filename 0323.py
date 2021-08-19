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

2. UnionFind: O(V+E) time | O(V) space
"""




import unittest
import collections
from typing import List
class Solution(object):
    def countComponents(self, n: int, edges: List[List[int]]) -> int:  # dfs
        graph = collections.defaultdict(list)  # adj. list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        count = 0
        visited = set()

        for node in range(n):
            if node not in visited:
                self.dfs(node, visited, graph)
                count += 1
        return count

    def dfs(self, node, visited, graph):
        if node in graph:  # if node has no edges, it won't be in graph
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    self.dfs(neighbor, visited, graph)

    def countComponents2(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1] * n

        def find(u):
            while u != parents[u]:
                parents[u] = parents[parents[u]]
                u = parents[u]
            return u
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return 0
            if ranks[pu] < ranks[pv]:
                parents[pu] = pv
            elif ranks[pv] < ranks[pu]:
                parents[pv] = pu
            else:
                parents[pv] = pu
                ranks[pu] += 1
            return 1

        result = n
        for source, target in edges:
            result -= union(source, target)
        return result
    


    # Unit Tests
funcs = [Solution().countComponents, Solution().countComponents2]


class TestCountComponents(unittest.TestCase):
    def testCountComponents1(self):
        for func in funcs:
            n = 5
            edges = [[0, 1], [1, 2], [3, 4]]
            self.assertEqual(
                func(n=n, edges=edges), 2)


if __name__ == "__main__":
    unittest.main()
