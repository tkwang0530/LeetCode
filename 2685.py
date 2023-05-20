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
    def __init__(self, total):
        self.parents = [i for i in range(total)]
        self.ranks = [1 for _ in range(total)]
        self.parentsCount = 0
        
    def find(self, u):
        if u != self.parents[u]:
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
        self.parentsCount -= 1
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        output = []
        unionFind = UnionFind(m*n)
        def findIndex(row, col):
            return row*n + col
        
        landsSet = set()
        for row, col in positions:
            if (row, col) not in landsSet:
                unionFind.parentsCount += 1
            landsSet.add((row, col))
            for diffRow, diffCol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nextRow, nextCol = row+diffRow, col+diffCol
                if nextRow in (-1,m) or nextCol in (-1,n):
                    continue
                
                if (nextRow, nextCol) not in landsSet:
                    continue
                
                unionFind.union(findIndex(row, col), findIndex(nextRow, nextCol))
            output.append(unionFind.parentsCount)
                
        return output

# Unit Tests
import unittest
funcs = [Solution().numIslands2]
class TestNumIslands2(unittest.TestCase):
    def testNumIslands2_1(self):
        for func in funcs:
            m = 3
            n = 3
            positions = [[0,0],[0,1],[1,2],[2,1]]
            self.assertEqual(func(m=m, n=n, positions=positions), [1,1,2,3])

    def testNumIslands2_2(self):
        for func in funcs:
            m = 1
            n = 1
            positions = [[0,0]]
            self.assertEqual(func(m=m, n=n, positions=positions), [1])

if __name__ == "__main__":
    unittest.main()
