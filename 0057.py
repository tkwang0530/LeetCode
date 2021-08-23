"""
57. Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary)

You may assume that the intervals were initally sorted according to their start times.

Example1:
    Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
    Output: [[1,5],[6,9]]
Example2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example3:
    Input: intervals = [], newInterval = [5,7]
    Output: [[5,7]]
Example4:
    Input: intervals = [[1,5]], newInterval = [2,3]
    Output: [[1,5]]
Example5:
    Input: intervals = [[1,5]], newInterval = [2,7]
    Output: [[1,7]]
"""

"""
Note:
1. Brute-Force: O(n) time | O(n) space
collect and merge while going over the intervals once
2. Brute-Force with improvement: O(n) time | O(n) space
collect and merge while going over the intervals once, but return it earlier when possible
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        left, right = [], []
        for interval in intervals:
            if interval[1] < start:
                left.append(interval)
            elif interval[0] > end:
                right.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        return left + [[start, end]] + right

    def insert2(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        res = []
        for i, interval in enumerate(intervals):
            if interval[1] < start:
                res.append(interval)
            elif interval[0] > end:
                res.append([start, end])
                return res + intervals[i:]  # can return earlier
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        res.append([start, end])
        return res


# Unit Tests
import unittest
funcs = [Solution().insert, Solution().insert2]

class TestInsert(unittest.TestCase):
    def testInsert1(self):
        for func in funcs:
            self.assertEqual(
                func(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]), [[1, 5], [6, 9]]
            )


    def testInsert2(self):
        for func in funcs:
            self.assertEqual(
                func(
                    intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                    newInterval=[4, 8],
                ),
                [[1, 2], [3, 10], [12, 16]],
            )

    def testInsert3(self):
        for func in funcs:
            self.assertEqual(
                func(
                    intervals=[],
                    newInterval=[5, 7],
                ),
                [[5, 7]],
            )


    def testInsert4(self):
        for func in funcs:
            self.assertEqual(
                func(
                    intervals=[[1, 5]],
                    newInterval=[2, 3],
                ),
                [[1, 5]],
            )

    def testInsert5(self):
        for func in funcs:
            self.assertEqual(
                func(
                    intervals=[[1, 5]],
                    newInterval=[2, 7],
                ),
                [[1, 7]],
            )

if __name__ == "__main__":
    unittest.main()