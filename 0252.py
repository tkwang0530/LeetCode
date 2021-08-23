"""
252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times 
[[s1, e1], [s2, e2], ...] (si < ei), determine if a person could attend all meetings.

Example1:
Input: [[0, 30], [5, 10], [15, 20]]
Output: false

Example2:
Input: [[7, 10], [2, 4]]
Output: true
"""

"""
Note:
1. Sort + One pass: O(nlogn) time | O(n) space
Sort by start time, check if two adjacent meetings overlapped.
They overlapped if the first meeting end time > the second meeting start time.

2. Sort + One pass (use while): O(nlogn) time | O(n) space
"""

import unittest
from typing import List
class Solution(object):
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        prevEnd = float("-inf")
        for interval in intervals:
            if interval[0] < prevEnd:
                return False
            prevEnd = interval[1]
        return True

    def canAttendMeetings2(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] > intervals[i][1]:
                return False
            i += 1
        return True


# Unit Tests
funcs = [Solution().canAttendMeetings]


class TestCanAttendMeetings(unittest.TestCase):
    def testCanAttendMeetings1(self):
        for func in funcs:
            intervals = [[0, 30], [5, 10], [15, 20]]
            self.assertEqual(
                func(intervals=intervals), False)

    def testCanAttendMeetings2(self):
        for func in funcs:
            intervals = [[7, 10], [2, 4]]
            self.assertEqual(
                func(intervals=intervals), True)


if __name__ == "__main__":
    unittest.main()
