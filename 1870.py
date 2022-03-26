"""
1870. Minimum Speed to Arrive on Time
You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the i-th train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

- For example, if the 1-st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.

Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time.

Tests are generated such that the answer will not exceed 10^7 and hour will have at most two digits after the decimal point.

Example1:
Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.

Example2:
Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3:
- The first train ride takes 1/3 = 0.33333 hours.
- Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
- You will arrive at the 2.66667 hour mark.

Example3:
Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.

Constraints:
n == dist.length
1 <= n <= 10^5
1 <= dist[i] <= 10^5
1 <= hour <= 10^9
There will be at most two digits after the decimal point in hour.
"""

"""
Note:
1. Binary Search: O(nlogm) time | O(1) space - where n is the length of dist and m is the range of speed
"""

import math
from typing import List
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        maxSpeed = max(dist)
        if hour == int(hour):
            if hour < len(dist):
                return -1
        else:
            if hour < len(dist) - 1:
                return -1
            # velocity = dist / time
            endSpeed = math.ceil(dist[-1] / (hour - int(hour)))
            maxSpeed = max(maxSpeed, endSpeed)
        
        left, right = 1, maxSpeed+1
        candidate = maxSpeed
        while left < right:
            speed = left + (right - left) // 2
            currentHour = 0
            for i, d in enumerate(dist):
                if i == len(dist) - 1:
                    time = d / speed
                else:
                    time = d // speed if d % speed == 0 else d // speed + 1
                currentHour += time
            
            if currentHour == hour:
                candidate = speed
                break
            elif currentHour > hour:
                left = speed + 1
            else:
                candidate = min(candidate, speed)
                right = speed
        return candidate


# Unit Tests
import unittest
funcs = [Solution().minSpeedOnTime]


class TestMinSpeedOnTime(unittest.TestCase):
    def testMinSpeedOnTime1(self):
        dist = [1,3,2]
        hour = 6
        for func in funcs:
            self.assertEqual(func(dist=dist, hour=hour), 1)

    def testMinSpeedOnTime2(self):
        dist = [1,3,2]
        hour = 2.7
        for func in funcs:
            self.assertEqual(func(dist=dist, hour=hour), 3)

    def testMinSpeedOnTime3(self):
        dist = [1,3,2]
        hour = 1.9
        for func in funcs:
            self.assertEqual(func(dist=dist, hour=hour), -1)

    def testMinSpeedOnTime4(self):
        dist = [1,1,100000]
        hour = 2.01
        for func in funcs:
            self.assertEqual(func(dist=dist, hour=hour), 10000000)

    def testMinSpeedOnTime5(self):
        dist = [6,10,5,1,8,9,2]
        hour = 34.0
        for func in funcs:
            self.assertEqual(func(dist=dist, hour=hour), 2)

    def testMinSpeedOnTime6(self):
        dist = [47,40,31,8,31,73,11,11,94,63,9,98,69,99,17,17,85,61,71,22,34,68,78,55,28,70,97,94,89,26,92,40,52,86,84,48,57,67,58,16,32,29,9,44,3,76,71,30,76,29,1,10,91,81,8,30,9]
        hour = 73.58
        for func in funcs:
            self.assertEqual(func(dist=dist, hour=hour), 71)

if __name__ == "__main__":
    unittest.main()
