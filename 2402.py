"""
2402. Meeting Rooms III
description: https://leetcode.com/problems/meeting-rooms-iii/description/
"""

"""
Note:
1. 2 minHeap: O(nlogn + mlogm) time | O(n+m) space - where m is the length of array meetings
"""

from typing import List
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # readyMinHeap contains the ready room index for meetings
        readyMinHeap = [room for room in range(n)]
        heapq.heapify(readyMinHeap)

        # readyMinHeap contains the rooms in use with [endTime, roomIdx] as element
        roomsMinHeap = [] # [endTime, roomIdx]
        roomUsedCount = [0] * n
        t = 0
        for start, end in sorted(meetings):
            t = max(t, start)
            # update rooms' status
            while roomsMinHeap and roomsMinHeap[0][0] <= t:
                _, r = heapq.heappop(roomsMinHeap)
                heapq.heappush(readyMinHeap, r)

            # if there is ready room
            if readyMinHeap:
                r = heapq.heappop(readyMinHeap)
                heapq.heappush(roomsMinHeap, [t+(end-start), r]) 
            else:
                # otherwise, update the current time to the first ending meeting room
                t, r = heapq.heappop(roomsMinHeap)
                heapq.heappush(roomsMinHeap, [t + end - start, r])
            roomUsedCount[r] += 1
        return roomUsedCount.index(max(roomUsedCount))

# Unit Tests
import unittest
funcs = [Solution().mostBooked]


class TestMostBooked(unittest.TestCase):
    def testMostBooked1(self):
        for func in funcs:
            n = 2
            meetings = [[0,10],[1,5],[2,7],[3,4]]
            self.assertEqual(func(n=n, meetings=meetings), 0)

    def testMostBooked2(self):
        for func in funcs:
            n = 3
            meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
            self.assertEqual(func(n=n, meetings=meetings), 1)

if __name__ == "__main__":
    unittest.main()
