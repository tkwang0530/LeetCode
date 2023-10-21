"""
1610. Maximum Number of Visible Points
description: https://leetcode.com/problems/maximum-number-of-visible-points/description/
"""

"""
Note:
1. Sort + Sliding Window: O(nlogn) time | O(2n) space - where n is the length of array points
"""

from typing import List
import math
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        def getAngle(xDiff, yDiff):
            return math.atan2(yDiff, xDiff) * 180 / math.pi

        basedPoint = 0
        angles = []
        for x, y in points:
            if [x,y] == location:
                basedPoint += 1
                continue

            angles.append(getAngle(x-location[0],y-location[1]))

        maxCount = 0
        A = len(angles)
        for i in range(A):
            angles.append(angles[i]+360)
        angles.sort()

        right = 0
        for left in range(A):
            while right < len(angles) and angles[right]-angles[left] <= angle:
                right += 1
            maxCount = max(maxCount, right-left)
        return maxCount + basedPoint

# Unit Tests
import unittest
funcs = [Solution().visiblePoints]

class TestVisiblePoints(unittest.TestCase):
    def testVisiblePoints1(self):
        for visiblePoints in funcs:
            points = [[2,1],[2,2],[3,3]]
            angle = 90
            location = [1,1]
            self.assertEqual(visiblePoints(points=points, angle=angle, location=location), 3)

    def testVisiblePoints2(self):
        for visiblePoints in funcs:
            points = [[2,1],[2,2],[3,4],[1,1]]
            angle = 90
            location = [1,1]
            self.assertEqual(visiblePoints(points=points, angle=angle, location=location), 4)

    def testVisiblePoints3(self):
        for visiblePoints in funcs:
            points = [[1,0],[2,1]]
            angle = 13
            location = [1,1]
            self.assertEqual(visiblePoints(points=points, angle=angle, location=location), 1)

if __name__ == "__main__":
    unittest.main()