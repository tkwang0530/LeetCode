"""
1011. Capacity To Ship Packages Within D Days
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Constraints:
1 <= days <= weights.length <= 5 * 10^4
1 <= weights[i] <= 500
"""

"""
Note:
1. Binary Search: O(nlogw) time | O(1) space - where n is the length of weights and w is max(weights)*n - max(weights)
"""
from typing import List
class Solution(object):
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def condition(capacity):
            usedDay = 0
            currentWeight = 0
            for weight in weights:
                if currentWeight + weight > capacity:
                    currentWeight = weight
                    usedDay += 1
                elif currentWeight + weight == capacity:
                    currentWeight = 0
                    usedDay += 1
                else:
                    currentWeight += weight
            usedDay = usedDay + 1 if currentWeight > 0 else usedDay
            return usedDay <= days
        
        maxWeight = max(weights)
        left, right = maxWeight, maxWeight * len(weights) + 1
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Unit Tests
import unittest
funcs = [Solution().shipWithinDays]


class TestShipWithinDays(unittest.TestCase):
    def testShipWithinDays1(self):
        for func in funcs:
            weights = [1,2,3,4,5,6,7,8,9,10]
            days = 5
            self.assertEqual(func(weights=weights, days=days), 15)

    def testShipWithinDays2(self):
        for func in funcs:
            weights = [3,2,2,4,1,4]
            days = 3
            self.assertEqual(func(weights=weights, days=days), 6)

    def testShipWithinDays3(self):
        for func in funcs:
            weights = [1,2,3,1,1]
            days = 4
            self.assertEqual(func(weights=weights, days=days), 3)

if __name__ == "__main__":
    unittest.main()
