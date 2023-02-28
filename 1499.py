"""
1499. Max Value of Equation
You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [x_i, y_i] such that x_i < x_y for all 1 <= i < j <= points.length. You are also given an integer k

Return the maximum value of the equation y_i + y_j + |x_i - x_j| where |x_i - x_j| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy the constraint |x_i - x_j| <= k.

Example1:
Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.

Example2:
Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.

Constraints:
2 <= points.length <= 10^5
points[i].length == 2
-10^8 <= x_i, y_i <= 10^8
0 <= k <= 2 * 10^8
x_i < x_j for all 1 <= i < j <= points.length
x_i form a strictly increasing sequence.
"""

"""
Note:
1. maxHeap: O(nlogn) time | O(n) space - where n is the number of points
2. monotonic queue: O(n) time | O(n) space - where n is the number of points
"""




import collections
from typing import List
import unittest
import heapq
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # yi + yj + | xi - xj | = (yi - xi) + (yj + xj)
        # |x_i - x_j| <= k
        maxVal = float("-inf")
        maxHeap = []
        for x, y in points:
            # x - maxHeap = |x_i - x_j|
            # pop out invalid points
            while maxHeap and x - maxHeap[0][1] > k:
                heapq.heappop(maxHeap)

            if maxHeap:
                # -maxHeap[0][0] = (yi - xi)
                # y + x = y_j + x_j
                maxVal = max(maxVal, -maxHeap[0][0] + (y + x))

            heapq.heappush(maxHeap, (-(y - x), x))
        return maxVal

    def findMaxValueOfEquation2(self, points: List[List[int]], k: int) -> int:
        # yi + yj + | xi - xj | = (yi - xi) + (yj + xj)
        maxVal = float("-inf")
        queue = collections.deque()

        for x, y in points:
            while queue and x - queue[0][1] > k:
                queue.popleft()

            if queue:
                maxVal = max(maxVal, queue[0][0] + (y + x))

            # queue[-1][0] = (yi - xi)
            # pop out all candidates with smaller yi - xi
            while queue and queue[-1][0] <= y - x:
                queue.pop()

            queue.append((y - x, x))
        return maxVal


# Unit Tests
funcs = [Solution().findMaxValueOfEquation, Solution().findMaxValueOfEquation2]


class TestFindMaxValueOfEquation(unittest.TestCase):
    def testFindMaxValueOfEquation1(self):
        for func in funcs:
            points = [[1, 3], [2, 0], [5, 10], [6, -10]]
            k = 1
            self.assertEqual(func(points=points, k=k), 4)

    def testFindMaxValueOfEquation2(self):
        for func in funcs:
            points = [[0, 0], [3, 0], [9, 2]]
            k = 3
            self.assertEqual(func(points=points, k=k), 3)


if __name__ == "__main__":
    unittest.main()
