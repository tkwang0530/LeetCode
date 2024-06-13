"""
2477. Minimum Fuel Cost to Report to the Capital
description: https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/
"""

"""
Note:
1. dfs (preOrder +postOrder): O(n) time | O(n) space - where n is the number of cities
"""

import collections
from  typing import List, Tuple
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = collections.defaultdict(set)
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)

        
        def removePreCity(city, preCity):
            if preCity != -1:
                graph[city].remove(preCity)
            for neighbor in graph[city]:
                removePreCity(neighbor, city)


        removePreCity(0, -1)
        def dfs(city) -> Tuple[int]: # people, cars, fuels
            totalFuels = 0
            totalPeople = 1
            totalCars = 1
            for childCity in graph[city]:
                people, cars, fuels = dfs(childCity)
                totalFuels += fuels + cars
                totalPeople += people
                totalCars += cars

            return totalPeople, totalPeople//seats + (totalPeople%seats>0), totalFuels
        
        return dfs(0)[-1]

# Unit Tests
import unittest
funcs = [Solution().minimumFuelCost]
class TestMinimumFuelCost(unittest.TestCase):
    def testMinimumFuelCost1(self):
        for func in funcs:
            roads = [[0,1],[0,2],[0,3]]
            seats = 5
            self.assertEqual(func(roads, seats), 3)


    def testMinimumFuelCost2(self):
        for func in funcs:
            roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
            seats = 2
            self.assertEqual(func(roads, seats), 7)


    def testMinimumFuelCost3(self):
        for func in funcs:
            roads = []
            seats = 1
            self.assertEqual(func(roads, seats), 0)


if __name__ == "__main__":
    unittest.main()
