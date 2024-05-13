"""
3112. Minimum Time to Visit Disappearing Nodes
description: https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/description/
"""

"""
Note:
1. dijkstra algorithm (optimized): O(E+ElogE) time | O(n+E) space - where n is the number of nodes and E is the number of edges
"""

import unittest, collections, heapq
from typing import List
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = min(w, graph[u].get(v, float("inf")))
            graph[v][u] = min(w, graph[v].get(u, float("inf")))

        nodeMinCost = [float("inf")] * n
        nodeMinCost[0] = 0
        minHeap = [(0, 0)] # (cost, node)
        while minHeap:
            currentCost, node = heapq.heappop(minHeap)
            if currentCost > nodeMinCost[node]:
                continue
            for nextNode, cost in graph[node].items():
                if nodeMinCost[nextNode] <= cost + currentCost:
                    continue
                if cost + currentCost >= disappear[nextNode]:
                    continue
                nodeMinCost[nextNode] = cost + currentCost
                heapq.heappush(minHeap, (cost+currentCost, nextNode))

        return [x if x < float("inf") else -1 for x in nodeMinCost]


# Unit Tests
import unittest
funcs = [Solution().minimumTime]
class TestMinimumTime(unittest.TestCase):
    def testMinimumTime1(self):
        for func in funcs:
            n = 3
            edges = [[0,1,2],[1,2,1],[0,2,4]]
            disappear = [1,1,5]
            self.assertEqual(func(n, edges, disappear), [0,-1,4])

    def testMinimumTime2(self):
        for func in funcs:
            n = 3
            edges = [[0,1,2],[1,2,1],[0,2,4]]
            disappear = [1,3,5]
            self.assertEqual(func(n, edges, disappear), [0,2,3])

    def testMinimumTime3(self):
        for func in funcs:
            n = 2
            edges = [[0,1,1]]
            disappear = [1,1]
            self.assertEqual(func(n, edges, disappear), [0,-1])
if __name__ == "__main__":
    unittest.main()
