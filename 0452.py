"""
452. Minimum Number of Arrows to Burst Balloons
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [x_start, x_end] denotes a balloon whose horizontal diameter stretches between x_start and x_end. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with x_start and x_end is burst by an arrow shot at x_start <= x <= x_end. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
"""

"""
Note:
1. Greedy: O(nlogn) time | O(1) space
Sort the points with x_end ascendingly
Only count valid intervals we need, and skip overlapping intervals
return the count
(always shot the end of the balloon if its x_start is larger than the previous x_end (previous shot position))
"""

from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        count, preEnd = 0, -float("inf")
        for start, end in points:
            if start > preEnd:
                count += 1
                preEnd = end
        return count

# Unit Tests
import unittest
funcs = [Solution().findMinArrowShots]
class TestFindMinArrowShots(unittest.TestCase):
    def testFindMinArrowShots1(self):
        for func in funcs:
            points = [[10,16],[2,8],[1,6],[7,12]]
            self.assertEqual(func(points=points), 2)

    def testFindMinArrowShots2(self):
        for func in funcs:
            points = [[1,2],[3,4],[5,6],[7,8]]
            self.assertEqual(func(points=points), 4)

    def testFindMinArrowShots3(self):
        for func in funcs:
            points = [[1,2],[2,3],[3,4],[4,5]]
            self.assertEqual(func(points=points), 2)

if __name__ == "__main__":
    unittest.main()
