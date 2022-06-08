"""
774. Minimize Max Distance to Gas Station
You are given an integer array stations that represents the positions of the gas stations on the x-axis. You are also given an integer k.

You should add k new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

Let penalty() be the maximum distance between adjacent gas stations after adding the k new stations.

Return the smallest possible value of penalty(). Answer within 10^-6 of the actual answer will be accepted.

Example1:
Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
Output: 0.50000

Example2:
Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
Output: 14.00000

Constraints:
10 <= stations.length <= 2000
0 <= stations[i] <= 10^8
stations is sorted in a strictly increasing order.
1 <= k <= 10^6
"""

"""
Note:
1. maxHeap: O(klogn) time | O(n) space - where n is the length of array stations
2. Binary Search: O(nlog(L)) time | O(n) space - where n is the length of array stations and L is the stations[-1] - stations[0]
"""

from typing import List
import heapq, math
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        maxHeap = [] # (distance/(spliters+1), distance, spliters)
        for i in range(1, len(stations)):
            distance = stations[i] - stations[i-1]
            maxHeap.append((-distance, distance, 0))
            
        heapq.heapify(maxHeap)
        
        while k > 0:
            _, distance, spliters = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-(distance/(spliters+2)), distance, spliters+1))
            k -= 1
        
        return abs(maxHeap[0][0])

    def minmaxGasDist2(self, stations: List[int], k: int) -> float:
        def condition(d):
            return sum([math.ceil((stations[i+1] - stations[i]) / d) - 1 for i in range(len(stations) - 1)]) <= k

        left, right = 0, stations[-1] - stations[0]
        while right - left > 1e-6:
            mid = left + (right - left) / 2
            if condition(mid):
                right = mid
            else:
                left = mid
        return left
# Unit Tests
import unittest
funcs = [Solution().minmaxGasDist, Solution().minmaxGasDist2]
class TestMinmaxGasDist(unittest.TestCase):
    def testMinmaxGasDist1(self):
        for func in funcs:
            stations = [1,2,3,4,5,6,7,8,9,10]
            k = 9
            self.assertAlmostEqual(func(stations=stations, k=k), 0.5, delta=1e-6)

    def testMinmaxGasDist2(self):
        for func in funcs:
            stations = [23,24,36,39,46,56,57,65,84,98]
            k = 1
            self.assertAlmostEqual(func(stations=stations, k=k), 14, delta=1e-6)

if __name__ == "__main__":
    unittest.main()
