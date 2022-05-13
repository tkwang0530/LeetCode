"""
1135. Connecting Cities With Minimum Cost
There are n cities labeled from 1 to n. You are given the integer n and an array connections
where connections[i] = [x_i, y_i, cost_i] indicates that the cost of connecting city x_i and city y_i (bidirectional connection) is cost_i.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1

The cost is the sum of the connections' costs used.

Example1:
Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.

Example2:
Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.

Constraints:
1 <= n <= 10^4
1 <= connections.length <= 10^4
connections[i].length == 3
1 <= x_i, y_i <= n
x_i != y_i
0 <= cost_i <= 10^5
"""

"""
Note:
1. Prim's Algorithm: O(E+ElogE) time | O(V+E+2E) space
2. Kruskal's Algorithm: o(E+ElogE) time | O(n) space
"""
import collections, heapq
from typing import List
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
        elif self._ranks[pv] < self._ranks[pu]:
            self._parents[pv] = pu
        else:
            self._parents[pv] = pu
            self._ranks[pu] += 1
        return True

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for src, dest, cost in connections:
            graph[src].append((cost, dest))
            graph[dest].append((cost, src))

        minHeap = [(0, 1)]
        totalCost = 0
        visited = set()

        while minHeap:
            cost, city = heapq.heappop(minHeap)
            if city in visited:
                continue
            totalCost += cost
            visited.add(city)
            for neighborCost, neighbor in graph[city]:
                if neighbor in visited:
                    continue
                heapq.heappush(minHeap, (neighborCost, neighbor))
        return totalCost if len(visited) == n else -1

    def minimumCost2(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        unionFind = UnionFindSet(n)
        connections.sort(key = lambda x: x[2])

        totalCost = 0
        unionCount = 0
        for x, y, cost in connections:
            if unionFind.union(x, y):
                totalCost += cost
                unionCount += 1
        
        return totalCost if unionCount == n - 1 else -1




# Unit Tests
import unittest
funcs = [Solution().minimumCost, Solution().minimumCost2]

class TestMinimumCost(unittest.TestCase):
    def testMinimumCost1(self):
        for func in funcs:
            n = 3
            connections = [[1,2,5],[1,3,6],[2,3,1]]
            self.assertEqual(func(n=n, connections=connections), 6)

    def testMinimumCost2(self):
        for func in funcs:
            n = 4
            connections = [[1,2,3],[3,4,4]]
            self.assertEqual(func(n=n, connections=connections), -1)

if __name__ == "__main__":
    unittest.main()