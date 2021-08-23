"""
253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times 
[[s1, e1], [s2, e2], ...] (si < ei), find the minimum number of conference rooms required.

Example1:
Input: [[0, 30], [5, 10], [15, 20]]
Output: 2

Example2:
Input: [[7, 10], [2, 4]]
Output: 1
"""

"""
Note:
1. Use minHeap: O(nlogn) time | O(n) space
the idea is if the room is used, mark the room with its end time.
(1) sort the intervals with their starting time
(2) initially put the first interval's ending time to our minHeap (rooms)
(3) traverse the intervals, when interval's starting time is less than the minimum ending time in the minHeap, heappop one out, and heappush that interval's ending time into the minHeap
(4) after traverse, return the length of the heap
"""

import heapq
import unittest
from typing import List
class Solution(object):
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[0])
        rooms = [intervals[0][1]]
        i = 1
        while i < len(intervals):
            if rooms[0] <= intervals[i][0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
            i += 1
        return len(rooms)


# Unit Tests
funcs = [Solution().minMeetingRooms]


class TestMinMeetingRooms(unittest.TestCase):
    def testMinMeetingRooms1(self):
        for func in funcs:
            intervals = [[0, 30], [5, 10], [15, 20]]
            self.assertEqual(
                func(intervals=intervals), 2)

    def testMinMeetingRooms2(self):
        for func in funcs:
            intervals = [[7, 10], [2, 4]]
            self.assertEqual(
                func(intervals=intervals), 1)


if __name__ == "__main__":
    unittest.main()
