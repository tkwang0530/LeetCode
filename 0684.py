"""
684. Redundant Connection
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two "different" vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [a_i, b_i] indicates that there is an edge between nodes a_i and b_i in the graph

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example1:
1 -  2
|   /
3
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= a_i, b_i <= edges.length
a_i != b_i
There are no repeated edges.
The given graph is connected.
"""

"""
Note:
1. Recursive DFS: O(n^2) time | O(n) space
use DFS to check whether u, v are already connected
2. Union-Find (using manual UnionFindSet): O(n) time | O(n) space
"""

from collections import defaultdict
from typing import List
import unittest


class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n+1)]
        self._ranks = [1 for _ in range(n+1)]

    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:
            self._parents[pv] = pu
            self._ranks[pu] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for source, target in edges:
            visited = set()
            if self.hasPath(source, target, graph, visited):
                return [source, target]
            graph[source].append(target)
            graph[target].append(source)
        return []
            
    def hasPath(self, source, target, graph, visited) -> bool:
        if source == target:
            return True
        visited.add(source)
        if not graph[source] or not graph[target]:
            return False
        for neighbor in graph[source]:
            if neighbor in visited:
                continue
            if self.hasPath(neighbor, target, graph, visited):
                return True
        return False
    
    def findRedundantConnection2(self, edges):
        unionFindSet = UnionFindSet(len(edges))
        for source, target in edges:
            if not unionFindSet.union(source, target):
                return  [source, target]
        return []

    

# Unit Tests
funcs = [Solution().findRedundantConnection, Solution().findRedundantConnection2]


class TestFindRedundantConnection(unittest.TestCase):
    def testFindRedundantConnection1(self):
        for func in funcs:
            edges = [[1,2],[1,3],[2,3]]
            self.assertEqual(func(edges=edges), [2, 3])

    def testFindRedundantConnection2(self):
        for func in funcs:
            edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
            self.assertEqual(func(edges=edges), [1, 4])

if __name__ == "__main__":
    unittest.main()
