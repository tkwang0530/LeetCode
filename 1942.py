"""
1942. The Number of the Smallest Unoccupied Chair
description: https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/
"""

"""
Note:
1. bst + minHeap: O(nlogn) time | O(n) space - where n is the length of array times 
ref: https://www.youtube.com/watch?v=3pTEJ1vzgSI
"""

import heapq
from typing import List
from sortedcontainers import SortedList
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        availables = SortedList([i for i in range(n)])
        occupied = [] # minHeap (leaving, seat)
        infos = [(arrival, leaving, p) for p, (arrival, leaving) in enumerate(times)]
        infos.sort()
        for arrival, leaving, p in infos:
            # handle leaving
            while occupied and occupied[0][0] <= arrival:
                _, seat = heapq.heappop(occupied)
                availables.add(seat)

            # take a seat
            seat = availables[0]
            availables.remove(seat)
            heapq.heappush(occupied, (leaving, seat))
            if p == targetFriend:
                return seat
        return 0

funcs = [Solution().smallestChair]

import unittest
class TestSmallestChair(unittest.TestCase):
    def testSmallestChair1(self):
        for func in funcs:
            times = [[1,4],[2,3],[4,6]]
            targetFriend = 1
            self.assertEqual(func(times=times, targetFriend=targetFriend), 1)

    def testSmallestChair2(self):
        for func in funcs:
            times = [[3,10],[1,5],[2,6]]
            targetFriend = 0
            self.assertEqual(func(times=times, targetFriend=targetFriend), 2)

if __name__ == "__main__":
    unittest.main()
