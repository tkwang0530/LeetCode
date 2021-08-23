"""
759. Employee Free Time
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).
Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Example1:
Input: [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
Output: [[3, 4]]
Explanation: There are a total of three employees, and all common free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example2:
Input: [[[1, 3], [6, 7]], [[2, 4]], [[2,5], [9, 12]]]
Output: [[5, 6], [7, 9]]
"""

"""
Note:
1. Sort + one pass: O(nlogn) time | O(n)
where n is the number of intervals in the schedule
(1) append all employee's intervals into a single list called "intervals"
(2) sort intervals with their starting time
(3) traverse the intervals, and if the currStart > preEnd, that is there exists free time, so we have to append the Interval(preEnd, currStart) into the result list (update the preEnd = max(preEnd, currEnd))
"""

import unittest
from typing import List

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __str__(self):
        return f"({self.start},{self.end})"

class Solution(object):
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        if not schedule:
            return []
        result, intervals = [], []

        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start, interval.end])

        intervals.sort(key = lambda x: x[0])
        i = 1
        prevEnd = intervals[0][1]

        while i < len(intervals):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
            if currStart > prevEnd:
                result.append(Interval(prevEnd, currStart))
            prevEnd = max(prevEnd, currEnd)
            i += 1
        return result


# Unit Tests
funcs = [Solution().employeeFreeTime]


class TestEmployeeFreeTime(unittest.TestCase):
    def testEmployeeFreeTime1(self):
        for func in funcs:
            schedule = [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]
            self.assertEqual(repr(func(schedule=schedule)), repr([Interval(3, 4)]))

    def testEmployeeFreeTime2(self):
        for func in funcs:
            schedule = [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]]
            self.assertEqual(repr(func(schedule=schedule)), repr([Interval(5, 6), Interval(7, 9)]))

if __name__ == "__main__":
    unittest.main()
