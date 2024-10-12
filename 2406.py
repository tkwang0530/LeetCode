"""
2406. Divide Intervals Into Minimum Number of Groups
description: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/
"""

"""
Note:
1. Sort + minHeap: O(nlogn) time | O(n) space - where n is the length of array intervals
"""

import heapq
from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minTails = []
        for left, right in intervals:
            if not minTails:
                heapq.heappush(minTails, right)
                continue

            tail = minTails[0]
            heapq.heappush(minTails, right)
            if tail <= left-1:
                heapq.heappop(minTails)
        
        return len(minTails)

funcs = [Solution().minGroups]

import unittest
class TestMinGroups(unittest.TestCase):
    def testMinGroups1(self):
        for func in funcs:
            intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
            self.assertEqual(func(intervals=intervals), 3)

    def testMinGroups2(self):
        for func in funcs:
            intervals = [[1,3],[5,6],[8,10],[11,13]]
            self.assertEqual(func(intervals=intervals), 1)

if __name__ == "__main__":
    unittest.main()
