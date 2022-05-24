"""
1094. Car Pooling
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengers_i, from_i, to_i] indicates that the i-th trip has numPassengers_i passengers passengers and the locations to pick them up and drop them off are from_i and to_i respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Constraints:
1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengers_i <= 100
0 <= from_i < to_i <= 1000
1 <= capacity <= 10^5
"""

"""
Note:
1. line sweep: O(nlogn) time | O(n) space - where n is the length of array trips
"""
import collections
from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locIncreasePeoples = collections.defaultdict(int)
        for people, start, end in trips:
            locIncreasePeoples[start] += people
            locIncreasePeoples[end] -= people
        
        currentPeople = 0
        for loc in sorted(locIncreasePeoples.keys()):
            currentPeople += locIncreasePeoples[loc]
            if currentPeople > capacity:
                return False
        return True

# Unit Tests
import unittest
funcs = [Solution().carPooling]
class TestCarPooling(unittest.TestCase):
    def testCarPooling1(self):
        for func in funcs:
            trips = [[2,1,5],[3,3,7]]
            capacity = 4
            self.assertEqual(func(trips=trips, capacity=capacity), False)

    def testCarPooling2(self):
        for func in funcs:
            trips = [[2,1,5],[3,3,7]]
            capacity = 5
            self.assertEqual(func(trips=trips, capacity=capacity), True)


if __name__ == "__main__":
    unittest.main()
