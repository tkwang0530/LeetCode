"""
787. Cheapest Flights Within K Stops
There are n cities connected by some number of flights. You are given an array flights when flights[i] = [from_i, to_i, price_i] indicates that there is a flight from city from_i to city to_i with cost price_i .

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example1:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Constraints:
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= from_i, to_i < n
from_i != to_i
1 <= price_i <= 10^4
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
"""

"""
Note:
1. Bellman-Ford algorithm: O(Ek) time | O(n+E) space
"""

from typing import List
import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for source, target, cost in flights:
            graph[source].append((target, cost))

        minCostToCities = [float("inf")] * n
        minCostToCities[src] = 0

        visitedStop = 0
        while visitedStop <= k:
            temp = minCostToCities.copy()
            for city in range(n):
                if minCostToCities[city] == float("inf"):
                    continue
                for neighbor, cost in graph.get(city, []):
                    minCostToCities[neighbor] = min(minCostToCities[neighbor], temp[city] + cost)
            visitedStop += 1
        return minCostToCities[dst] if minCostToCities[dst] != float("inf") else -1
            

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
