"""
391. Perfect Rectangle
Given an array rectangles where rectangles[i] = [x_i, y_i, a_i, b_i] represents an axis-aligned represents an axis-aligned rectangle. The bottom-left point of the rectangle is [x_i, y_i] and the top-right point of it is (a_i, b_i).

Return true if all the rectangles together from an exact cover of a rectangular region.

Example1:
Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
Output: true
Explanation: All 5 rectangles together form an exact cover of a rectangular region.

Example2:
Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
Output: false
Explanation: Because there is a gap between the two rectangular regions.

Example3:
Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
Output: false
Explanation: Because two of the rectangles overlap with each other.

Constraints:
1 <= rectangles.length <= 2 * 10^4
rectangles[i].length == 4
-10^5 <= x_i, y_i, a_i, b_i <= 10^5
"""

""" 
1. HashTable: O(n) time | O(n) space - where n is the length of array rectangles
Find the bottom Left and top right poins, and calulate the target area
apply point check and area check
"""

from typing import List
import collections
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        bottomLeft = (float("inf"), float("inf"))
        topRight = (-float("inf"), -float("inf"))
        runningArea = 0
        pointCounts = collections.defaultdict(int)
        for x1,y1,x2,y2 in rectangles:
            runningArea += (x2-x1)*(y2-y1)
            pointCounts[(x1,y1)] += 1
            pointCounts[(x1,y2)] += 1
            pointCounts[(x2,y1)] += 1
            pointCounts[(x2,y2)] += 1
            bottomLeft = min(bottomLeft, (x1, y1), key=lambda x: sum(x))
            topRight = max(topRight, (x2, y2), key=lambda x: sum(x))

        for (x, y), count in pointCounts.items():
            if x in (bottomLeft[0], topRight[0]) and y in (bottomLeft[1], topRight[1]):
                if count != 1:
                    return False
            else:
                if count % 2 == 1:
                    return False
        return  runningArea == (topRight[0]-bottomLeft[0]) * (topRight[1] - bottomLeft[1])

# Unit Tests
import unittest
funcs = [Solution().isRectangleCover]
class TestIsRectangleCover(unittest.TestCase):
    def testIsRectangleCover1(self):
        for func in funcs:
            rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
            self.assertEqual(func(rectangles=rectangles), True)

    def testIsRectangleCover2(self):
        for func in funcs:
            rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
            self.assertEqual(func(rectangles=rectangles), False)

    def testIsRectangleCover3(self):
        for func in funcs:
            rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
            self.assertEqual(func(rectangles=rectangles), False)

if __name__ == "__main__":
    unittest.main()
