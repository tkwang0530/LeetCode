"""
435. Non-overlapping Intervals
Given an array of intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= start_i < end_i <= 5 * 10^4
"""

"""
Note:
1. Greedy Algorithm: O(nlogn) time | O(n) time
(1) sort the intervals by the starting point
(2) traverse the intervals and in each run, if we found overlapping, keep the end with smaller value and remove the larger one

2. Greedy Algorithm: O(nlogn) time | O(n) time
(1) sort the intervals by the (ending point, starting point)
(2) traverse the intervals and in each run, if we found start > previous end, count+=1, otherwise update preEnd to end
"""

from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        removes = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                removes += 1
                prevEnd = min(prevEnd, end)
        return removes

    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        preEnd = -float("inf")
        removeCount = 0
        for start, end in intervals:
            if start < preEnd:
                removeCount += 1
            else:
                preEnd = end
        return removeCount

# Unit Tests
import unittest
funcs = [Solution().eraseOverlapIntervals, Solution().eraseOverlapIntervals2]


class TestEraseOverlapIntervals(unittest.TestCase):
    def testEraseOverlapIntervals1(self):
        for func in funcs:
            intervals = [[1,2],[2,3],[3,4],[1,3]]
            self.assertEqual(func(intervals=intervals), 1)

    def testEraseOverlapIntervals2(self):
        for func in funcs:
            intervals = [[1,2],[1,2],[1,2]]
            self.assertEqual(func(intervals=intervals), 2)

    def testEraseOverlapIntervals3(self):
        for func in funcs:
            intervals = [[1,2],[2,3]]
            self.assertEqual(func(intervals=intervals), 0)


if __name__ == "__main__":
    unittest.main()
