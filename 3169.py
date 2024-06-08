"""
3169. Count Days Without Meetings
description: https://leetcode.com/problems/count-days-without-meetings/description/
"""

""" 
Notes:
1. Sort: O(mlogm) time | O(m) space 
"""

from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        def merge(meetings) -> List[List[int]]:
            meetings.sort()
            preEnd = -float("inf")
            merged = []
            for start, end in meetings:
                if start <= preEnd:
                    merged[-1][1] = max(end, preEnd)
                else:
                    merged.append([start, end])
                preEnd = max(preEnd, end)
            return merged
        
        mergedMeetings = merge(meetings)
        preEnd = -float("inf")
        noMeetings = 0
        for start,end in mergedMeetings:
            if preEnd != -float("inf"):
                noMeetings += start-preEnd-1
            else:
                noMeetings += start-1
            preEnd = end
        return noMeetings + days - preEnd

# Unit Tests
import unittest
funcs = [Solution().countDays]

class TestCountDays(unittest.TestCase):
    def testCountDays1(self):
        for func in funcs:
            days = 10
            meetings = [[5,7],[1,3],[9,10]]
            self.assertEqual(func(days=days, meetings=meetings), 2)

    def testCountDays2(self):
        for func in funcs:
            days = 5
            meetings = [[2,4],[1,3]]
            self.assertEqual(func(days=days, meetings=meetings), 1)

    def testCountDays3(self):
        for func in funcs:
            days = 6
            meetings = [[1,6]]
            self.assertEqual(func(days=days, meetings=meetings), 0)

if __name__ == "__main__":
    unittest.main()
