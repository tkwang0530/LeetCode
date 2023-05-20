"""
2685. Count the Number of Complete Components
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

Example1:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.

Example2:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

Constraints:
1 <= n <= 50
0 <= edges.length <= n * (n-1) / 2
edges[i].length == 2
0 <= a_i, b_i <= n - 1
a_i != b_i
There are no repeated edges.
"""

"""
Note:
1. UnionFind + HashTable: O(n+E) time | O(n+E) space - where E is the length of array edges
"""
from typing import List
class UnionFind:
    def __init__(self, n: int, edges: List[List[int]]) -> None:
        self.edgeMap = [set() for _ in range(n)]
        self.ranks = [1 for _ in range(n)]
        self.nodes = [1 for _ in range(n)]
        self.parents = [i for i in range(n)]
        for node1, node2 in edges:
            node1, node2 = sorted([node1, node2])
            self.edgeMap[node1].add((node1, node2))
            self.edgeMap[node2].add((node1, node2))
    
    def find(self, u) -> int:
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

        if self.ranks[pv] > self.ranks[pu]:
            for edge in self.edgeMap[pu]:
                self.edgeMap[pv].add(edge)
            self.nodes[pv] += self.nodes[pu]
        else:
            for edge in self.edgeMap[pv]:
                self.edgeMap[pu].add(edge)
            self.nodes[pu] += self.nodes[pv]
        
        return True
        

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n, edges)
        for node1, node2 in edges:
            uf.union(node1, node2)

        total = 0
        for node in range(n):
            if uf.find(node) != node:
                continue

            N = uf.nodes[node]
            E = len(uf.edgeMap[node])
            total += ((N*(N-1)//2) == E) or (E == 0 and N == 1)
        return total

# Unit Tests
import unittest
funcs = [Solution().countCompleteComponents]
class TestCountCompleteComponents(unittest.TestCase):
    def testCountCompleteComponents1(self):
        for func in funcs:
            n = 6
            edges = [[0,1],[0,2],[1,2],[3,4]]
            self.assertEqual(func(n=n, edges=edges), 3)

    def testCountCompleteComponents2(self):
        for func in funcs:
            n = 6
            edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
            self.assertEqual(func(n=n, edges=edges), 1)

if __name__ == "__main__":
    unittest.main()
