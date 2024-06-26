"""
787. Cheapest Flights Within K Stops
description: https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
"""

"""
Note:
1. Bellman-Ford algorithm: O(Ek) time | O(n+E) space
ref: https://www.youtube.com/watch?v=5eIK3zUdYmE

2. BFS (layer order traversal): O(Ek) time | O(n+E) space
"""

import collections
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k+1):
            tmpPrices = prices.copy()
            for s, d, p in flights: # s=source, d=destination, p=price
                if prices[s] == float("inf"):
                    continue

                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
            
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cityMinCost = collections.defaultdict(lambda: float("inf"))
        graph = collections.defaultdict(list)
        for city, toCity, price in flights:
            graph[city].append((toCity, price))

        
        candidates = [(0,src)] # [(cost, city)]
        stops = -1
        while candidates and stops <= k:
            nextCandidates = []
            for cost, city in candidates:
                if cost < cityMinCost[city]:
                    cityMinCost[city] = cost
                    for toCity, price in graph[city]:
                        nextCandidates.append((price+cost, toCity))
            stops += 1
            candidates = nextCandidates
        return -1 if cityMinCost[dst] == float("inf") else cityMinCost[dst]

# Unit Tests
import unittest
funcs = [Solution().findCheapestPrice]

class TestFindCheapestPrice(unittest.TestCase):
    def testFindCheapestPrice1(self):
        for func in funcs:
            n = 3
            flights = [[0,1,100],[1,2,100],[0,2,500]]
            src = 0
            dst = 2
            k = 1
            self.assertEqual(func(n=n, flights=flights, src=src, dst=dst, k=k), 200)

    def testFindCheapestPrice2(self):
        for func in funcs:
            n = 3
            flights = [[0,1,100],[1,2,100],[0,2,500]]
            src = 0
            dst = 2
            k = 0
            self.assertEqual(func(n=n, flights=flights, src=src, dst=dst, k=k), 500)

    def testFindCheapestPrice3(self):
        for func in funcs:
            n = 4
            flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
            src = 0
            dst = 3
            k = 1
            self.assertEqual(func(n=n, flights=flights, src=src, dst=dst, k=k), 6)


if __name__ == "__main__":
    unittest.main()
