"""
2332. The Latest Time to Catch a Bus
description: https://leetcode.com/problems/the-latest-time-to-catch-a-bus/description/
"""

"""
Note:
1. Sort + Greedy: O(nlogn + mlogm) time | O(1) space - where n is the length of array buses and m is the length of array passengers
"""

from typing import List
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        n = len(buses)
        m = len(passengers)
        p = 0
        for i, busArrivalTime in enumerate(buses):
            seats = capacity
            while seats and p < m and passengers[p] <= busArrivalTime:
                p += 1
                seats -= 1
            
            if i < n - 1:
                continue

            # the last bus is full, we have to reach before the last person who is on board
            if seats == 0:
                p -= 1
                time = passengers[p]
                while p >= 0 and time == passengers[p]:
                    time -= 1
                    p -= 1
                return time
            else:
                # the last bus is not full, then we can reach the station, at the bus's departure time
                time = busArrivalTime
                p -= 1
                while p >= 0 and time == passengers[p]:
                    time -= 1
                    p -= 1
                return time
        return -1

# Unit Tests
import unittest
funcs = [Solution().latestTimeCatchTheBus]
class TestLatestTimeCatchTheBus(unittest.TestCase):
    def testLatestTimeCatchTheBus1(self):
        for func in funcs:
            buses = [10,20]
            passengers = [2,17,18,19]
            capacity = 2
            self.assertEqual(func(buses=buses, passengers=passengers, capacity=capacity), 16)

    def testLatestTimeCatchTheBus2(self):
        for func in funcs:
            buses = [20,30,10]
            passengers = [19,13,26,4,25,11,21]
            capacity = 2
            self.assertEqual(func(buses=buses, passengers=passengers, capacity=capacity), 20)

if __name__ == "__main__":
    unittest.main()
