"""
2662. Minimum Cost of a Path With Special Roads
description: https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/
"""

"""
Note:
1. dijkstra algorithm: O(p^2log(p^2)) time | O(p^2) space - where p is the distinct number of positions, could be up to (len(specialRoads)+2) * 2
"""

from typing import List
import heapq, collections
import unittest


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        pointSet = set()
        pointSet.add(tuple(start))
        pointSet.add(tuple(target))
        for x1,y1,x2,y2, _ in specialRoads:
            pointSet.add((x1,y1))
            pointSet.add((x2,y2))

        points = list(pointSet)
        n = len(points)
        graph = collections.defaultdict(dict)
        for i in range(n):
            for j in range(i+1, n):
                point1, point2 = points[i], points[j]
                cost = abs(point2[0]-point1[0]) + abs(point2[1]-point1[1])
                graph[point1][point2] = cost
                graph[point2][point1] = cost

        for x1, y1, x2, y2, cost in specialRoads:
            if (x1,y1) == (x2, y2):
                continue
            graph[(x1, y1)][(x2, y2)] = min(graph[(x1, y1)][(x2, y2)], cost)

        postMinCost = {tuple(start): 0}
        minHeap = [(0, start[0], start[1])]
        while minHeap:
            currentCost, x, y = heapq.heappop(minHeap)
            if (x, y) == tuple(target):
                return currentCost

            for nextX, nextY in graph[(x, y)].keys():
                cost = graph[(x, y)][(nextX, nextY)]
                if (nextX, nextY) in postMinCost and cost+currentCost >= postMinCost[(nextX, nextY)]:
                    continue
                postMinCost[(nextX, nextY)] = cost+currentCost
                heapq.heappush(minHeap, (currentCost+cost, nextX, nextY))
        return -1

# Unit Tests
funcs = [Solution().minimumCost]
class TestMinimumCost(unittest.TestCase):
    def testMinimumCost1(self):
        for func in funcs:
            start = [1,1]
            target = [4,5]
            specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
            self.assertEqual(func(start=start, target=target, specialRoads=specialRoads), 5)

    def testMinimumCost2(self):
        for func in funcs:
            start = [3,2]
            target = [5,7]
            specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
            self.assertEqual(func(start=start, target=target, specialRoads=specialRoads), 7)

if __name__ == "__main__":
    unittest.main()