"""
218. The Skyline Problem
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [left_i, right_i, height_i]
- left_i is the x coordinate of the left edge of the ith building.
- right_i is the x coordinate of the right edge of the ith building.
- height_i is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1], [x2, y2], ...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [..., [2, 3], [4, 5], [7, 5, [11, 5], [12, 7], ...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [..., [2, 3], [4, 5], [12, 7], ...]
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

Example2:
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]


Constraints:
1 <= buildings.length <= 10^4
0 <= left_i < right_i <= 2^31 - 1
1 <= height_i <= 2^31 - 1
buildings is sorted by left_i in non-decreasing order.
"""

"""
Note:
1. events and heap: O(nlogn) time | O(n) space
"""

from typing import List
from heapq import heappop, heappush
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # add start-building events
        events = [(L, -H, R) for L, R, H in buildings]

        # also add end-building events (acts as building with 0 height)
        events += list({(R, 0, 0) for _, R, _ in buildings})

        # and sort the events in left -> right order
        events.sort()

        result = [[0, 0]] # [x, height]

        live = [(0, float("inf"))] # [-height, ending position]
        for pos, negH, R in events:
            # 1. pop buildings that are already ended
            # 2. if it's the start-building event, make the building alive
            # 3. if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos:
                heappop(live)
            if negH:
                heappush(live, (negH, R))
            if result[-1][1] != -live[0][0]:
                result += [ [pos, -live[0][0]] ]
        return result[1:]

# Unit Tests
import unittest
funcs = [Solution().getSkyline]


class TestGetSkyline(unittest.TestCase):
    def testGetSkyline1(self):
        for func in funcs:
            buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
            self.assertEqual(func(buildings=buildings), [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]])

    def testGetSkyline2(self):
        for func in funcs:
            buildings = [[0,2,3],[2,5,3]]
            self.assertEqual(func(buildings=buildings), [[0,3],[5,0]])

if __name__ == "__main__":
    unittest.main()