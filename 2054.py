"""
2054. Two Best Non-Overlapping Events
description: https://leetcode.com/problems/two-best-non-overlapping-events/description/
"""

"""
Note:
1. SuffixMax + Sort + Binary Search:  O(nlogn) time | O(n) space - where n is the length of array events 
"""

from typing import List
import bisect
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        suffixMax = {} # maxValue after start (inclusive)
        maxValue = float("-inf")
        for i in range(n-1, -1, -1):
            start, _, value = events[i]
            maxValue = max(maxValue, value)
            suffixMax[start] = maxValue

        # get the next start after preEnd + 1 (inclusive)
        maxSum = 0
        for i, (start, end, value) in enumerate(events):
            nextStartIdx = bisect.bisect(events, [end+1,-1,-1], i+1)
            nextValue = 0
            if nextStartIdx != n:
                nextStart = events[nextStartIdx][0]
                nextValue = suffixMax[nextStart]
            maxSum = max(maxSum, value + nextValue)
        return maxSum

import unittest
funcs = [Solution().maxTwoEvents]

class TestMaxTwoEvents(unittest.TestCase):
    def testMaxTwoEvents1(self):
        for func in funcs:
            events = [[1,3,2],[4,5,2],[2,4,3]]
            self.assertEqual(func(events=events), 4)

    def testMaxTwoEvents2(self):
        for func in funcs:
            events = [[1,3,2],[4,5,2],[1,5,5]]
            self.assertEqual(func(events=events), 5) 

    def testMaxTwoEvents3(self):
        for func in funcs:
            events = [[1,5,3],[1,5,1],[6,6,5]]
            self.assertEqual(func(events=events), 8) 

if __name__ == "__main__":
    unittest.main()
