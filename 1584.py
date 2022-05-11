"""
1584. Min Cost to Connect All Points
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [x_i, y_i].

The cost of connecting two points [x_i, y_i] and [x_j, y_j] is the manhattan distance between them: |x_i - x_j| + |y_i - y_j|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Example2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:
1 <= points.length <= 1000
-10^6 <= x_i, y_i <= 10^6
All pairs (x_i, y_i) are distinct
"""

"""
Note:
1. Prim's Algorithm: O(n^2logn) time | O(n^2) space - where n is the length of points
(1) Create graph (adjacency list)
(2) Prim's algorithm with minHeap
"""
import collections, heapq
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = collections.defaultdict(list) # point: list of (cost, targetPoint)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((distance, j))
                graph[j].append((distance, i))
        
        # Prim's Algorithm
        totalCost = 0
        visited = set()
        minHeap = [(0, 0)] # (cost, point)
        while len(visited) < n:
            cost, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            totalCost += cost
            visited.add(point)
            for neighborCost, neighbor in graph[point]:
                if neighbor in visited:
                    continue
                heapq.heappush(minHeap, (neighborCost, neighbor))
        return totalCost

# Unit Tests
import unittest
funcs = [Solution().minCostConnectPoints]

class TestMinCostConnecPoints(unittest.TestCase):
    def testMinCostConnecPoints1(self):
        for func in funcs:
            points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
            self.assertEqual(func(points=points), 20)

    def testMinCostConnecPoints2(self):
        for func in funcs:
            points = [[3,12],[-2,5],[-4,1]]
            self.assertEqual(func(points=points), 18)

if __name__ == "__main__":
    unittest.main()