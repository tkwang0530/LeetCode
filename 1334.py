"""
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
description: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
"""

"""
Note:
1. Floyd Warshall: O(n^3) time | O(n^2) space
ref: https://www.youtube.com/watch?v=iE0tJ-8rPLQ
"""

from typing import List
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float("inf")] * n for _ in range(n)]

        for fromCity, toCity, weight in edges:
            dist[fromCity][toCity] = weight
            dist[toCity][fromCity] = weight

        for k in range(n):
            for u in range(n):
                for v in range(n):
                    dist[u][v] = min(dist[u][v], dist[u][k]+dist[k][v])

        minNeighbor = float("inf")
        candidate = -1
        for u in range(n):
            reachables = 0
            for v in range(n):
                if v != u and dist[u][v] <= distanceThreshold:
                    reachables += 1

            if reachables <= minNeighbor:
                minNeighbor = reachables
                candidate = u
        return candidate
# Unit Tests
import unittest
funcs = [Solution().findTheCity]

class TestFindTheCity(unittest.TestCase):
    def testFindTheCity1(self):
        for func in funcs:
            n = 4
            edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
            distanceThreshold = 4
            self.assertEqual(func(n=n, edges=edges, distanceThreshold=distanceThreshold), 3)

    def testFindTheCity2(self):
        for func in funcs:
            n = 5
            edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
            distanceThreshold = 2
            self.assertEqual(func(n=n, edges=edges, distanceThreshold=distanceThreshold), 0)

if __name__ == "__main__":
    unittest.main()
