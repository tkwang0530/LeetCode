"""
253. Meeting Rooms II
description: https://leetcode.com/problems/meeting-rooms-ii/description/
"""

"""
Note:
1. Use minHeap: O(nlogn) time | O(n) space
the idea is if the room is used, mark the room with its end time.
(1) sort the intervals with their starting time
(2) initially put the first interval's ending time to our minHeap (rooms)
(3) traverse the intervals, when interval's starting time is less than the minimum ending time in the minHeap, heappop one out, and heappush that interval's ending time into the minHeap
(4) after traverse, return the length of the heap

2. Use two sorted array: O(nlogn) time | O(n) space
(1) store start time and end time on different array "start" and "end"
(2) sort them respectively
(3) iterate through the two arrays
    increase the count by 1 and s+= 1 if start[s] < end[e] otherwise, count -= 1 and e+=1

3. Line Sweep: O(n+klogk) time | O(k) space - where n is the length of intervals and k is the number of unique timestamps
"""

import heapq
import collections
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

    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])
        result, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            result = max(result, count)
        return result

    def minMeetingRooms3(self, intervals: List[List[int]]) -> int:
        sweep = collections.defaultdict(int)
        for start, end in intervals:
            sweep[start] += 1
            sweep[end] -= 1
        
        minimumRooms = 0
        meetingRooms = 0
        for time in sorted(sweep.keys()):
            meetingRooms += sweep[time]
            minimumRooms = max(minimumRooms, meetingRooms)

        return minimumRooms


# Unit Tests
import unittest
funcs = [Solution().minMeetingRooms, Solution().minMeetingRooms2, Solution().minMeetingRooms3]


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
