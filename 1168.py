"""
1168. Optimize Water Distribution in a Village
There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i-1] (note the -1 due to 0-indexing), or pipe in water from another well to it.

The costs to lay pipes between houses are given by the array pipes where each pipes[j] = [house1_j, house2_j, cost_j] represents the cost to connect house1_j and house2_j together using a pipe. Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.

Return the minimum total cost to supply water to all houses.

Example1:
Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.

Example2:
Input: n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]
Output: 2
Explanation: We can supply water with cost two using one of the three options:
Option 1:
  - Build a well inside house 1 with cost 1.
  - Build a well inside house 2 with cost 1.
The total cost will be 2.
Option 2:
  - Build a well inside house 1 with cost 1.
  - Connect house 2 with house 1 with cost 1.
The total cost will be 2.
Option 3:
  - Build a well inside house 2 with cost 1.
  - Connect house 1 with house 2 with cost 1.
The total cost will be 2.
Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose the cheapest option. 

Constraints:
2 <= n <= 10^4
wells.length == n
0 <= wells[i] <= 10^5
1 <= pipes.length <= 10^4
pipes[j].length == 3
1 <= house1_j, house2_j <= n
0 <= cost_j <= 10^5
house1_j != house2_j
"""

"""
Note:
1. Prim's Algorithm: O(E+VlogV+VlogE) time | O(V+E) space
2. Kruskal's Algorithm: O((V+E)log(V+E)) time | O(V+E) space
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
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = collections.defaultdict(dict)
        for house1, house2, cost in pipes:
            if house2 in graph[house1]:
                graph[house1][house2] = min(graph[house1][house2], cost)
                graph[house2][house1] = min(graph[house2][house1], cost)
            else:
                graph[house1][house2] = cost
                graph[house2][house1] = cost

        totalCost = 0
        visited = set()
        
        minHeap = []
        for i, cost in enumerate(wells):
            house = i+1
            heapq.heappush(minHeap, (cost, house))
        
        while len(visited) < n:
            cost, house = heapq.heappop(minHeap)
            if house in visited:
                continue
            visited.add(house)
            totalCost += cost
            for neighbor, neighborCost in graph[house].items():
                if neighbor in visited:
                    continue
                heapq.heappush(minHeap, (neighborCost, neighbor))
        return totalCost

    def minCostToSupplyWater2(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        costHouses = [(cost, house1, house2) for house1, house2, cost in pipes]
        for i, cost in enumerate(wells):
            house = i + 1
            costHouses.append((cost, house, house))
        costHouses.sort()

        unionCount = 0
        totalCost = 0
        unionFind = UnionFindSet(n)
        house0 = 0
        for i in range(len(costHouses)):
            if unionCount == n:
                break
            
            cost, house1, house2 = costHouses[i]
            if house1 == house2:
                if unionFind.union(house1, house0):
                    totalCost += cost
                    unionCount += 1
                continue
            
            if unionFind.union(house1, house2):
                totalCost += cost
                unionCount += 1

        return totalCost
# Unit Tests
import unittest
funcs = [Solution().minCostToSupplyWater, Solution().minCostToSupplyWater2]

class TestMinCostToSupplyWater(unittest.TestCase):
    def testMinCostToSupplyWater1(self):
        for func in funcs:
            n = 3
            wells = [1,2,2]
            pipes = [[1,2,1],[2,3,1]]
            self.assertEqual(func(n=n, wells=wells, pipes=pipes), 3)

    def testMinCostToSupplyWater2(self):
        for func in funcs:
            n = 2
            wells = [1,1]
            pipes = [[1,2,1],[1,2,2]]
            self.assertEqual(func(n=n, wells=wells, pipes=pipes), 2)

    def testMinCostToSupplyWater3(self):
        for func in funcs:
            n = 5
            wells = [46012,72474,64965,751,33304]
            pipes = [[2,1,6719],[3,2,75312],[5,3,44918]]
            self.assertEqual(func(n=n, wells=wells, pipes=pipes), 131704)

    def testMinCostToSupplyWater4(self):
        for func in funcs:
            n = 6
            wells = [4625,65696,86292,68291,37147,7880]
            pipes = [[2,1,79394],[3,1,45649],[4,1,75810],[5,3,22340],[6,1,6222]]
            self.assertEqual(func(n=n, wells=wells, pipes=pipes), 204321)

    def testMinCostToSupplyWater5(self):
        for func in funcs:
            n = 10
            wells = [22238,38788,73611,22861,18865,52721,85325,98901,72035,74803]
            pipes = [[2,1,82145],[3,1,83958],[4,2,52824],[5,4,60736],[6,1,38042],[7,6,30343],[9,3,34316]]
            self.assertEqual(func(n=n, wells=wells, pipes=pipes), 451192)

if __name__ == "__main__":
    unittest.main()