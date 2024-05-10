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

3. Buckets Sort: O(max(start) + n) time | O(n) space

4. Line Sweep: O(n+klogk) time | O(k) space - where n is the length of intervals and k is the number of unique timestamps
"""

import collections
import unittest
from typing import List
class Solution(object):
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        preEnd = -1
        for start, end in intervals:
            if preEnd > start:
                return False
            preEnd = end
        return True

class Solution2:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] > intervals[i][1]:
                return False
            i += 1
        return True

class Solution3:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        maxStart = max([start for start, _ in intervals])
        buckets = [[] for _ in range(maxStart+1)]
        for start, end in intervals:
            buckets[start].append([start, end])
        
        sortedIntervals = []
        for start in range(maxStart+1):
            sortedIntervals.extend(buckets[start])

        preEnd = -1
        for start, end in sortedIntervals:
            if preEnd > start:
                return False
            preEnd = end
        return True

class Solution4:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sweepLine = collections.defaultdict(int)
        for start, end in intervals:
            sweepLine[start] += 1
            sweepLine[end] -= 1
        
        overLaps = 0
        for time in sorted(sweepLine.keys()):
            overLaps += sweepLine[time]
            if overLaps > 1:
                return False
        return True

# Unit Tests
funcs = [Solution().canAttendMeetings, Solution2().canAttendMeetings, Solution3().canAttendMeetings, Solution4().canAttendMeetings]


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
