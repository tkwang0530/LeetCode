"""
743. Network Delay Time
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (u_i, v_i, w_i), where u_i is the source node, v_i is the target node, and w_i is the time it takes for a signal to travel from source to target

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= u_i, v_i <= n
u_i != v_i
0 <= w_i <= 100
All the pairs (u_i, v_i) are unique. (i.e., no multiple edges.)
"""

"""
Note:
1. Dijkstra's algorithm (minHeap): O(ElogV) time |  O(V+E)
"""

from collections import defaultdict
import heapq
from typing import List
import unittest
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for source, target, weight in times:
            edges[source].append((target, weight))
        
        minHeap = [(0, k)]
        heapq.heapify(minHeap)
        visited = set()
        t = 0
        while len(minHeap) > 0:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t, weight)
            for neighbor, weightToNeighbor in edges[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (weight + weightToNeighbor, neighbor))
        return t if len(visited) == n else -1


# Unit Tests
funcs = [Solution().networkDelayTime]


class TestNetworkDelayTime(unittest.TestCase):
    def testNetworkDelayTime1(self):
        for func in funcs:
            times = [[2,1,1],[2,3,1],[3,4,1]]
            n = 4
            k = 2
            self.assertEqual(func(times=times, n=n, k=k), 2)

    def testNetworkDelayTime2(self):
        for func in funcs:
            times = [[1,2,1]]
            n = 2
            k = 1
            self.assertEqual(func(times=times, n=n, k=k), 1)

    def testNetworkDelayTime3(self):
        for func in funcs:
            times = [[1,2,1]]
            n = 2
            k = 2
            self.assertEqual(func(times=times, n=n, k=k), -1)

    def testNetworkDelayTime4(self):
        for func in funcs:
            times = [[1,2,1],[2,1,3]]
            n = 2
            k = 2
            self.assertEqual(func(times=times, n=n, k=k), 3)


if __name__ == "__main__":
    unittest.main()
