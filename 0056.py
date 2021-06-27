"""
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input

Example1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

"""
Note:
1. Sort + one pass: O(nlogn) time | O(n) space
"""




import unittest
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals, key=lambda x: x[0])
        currentInterval = sortedIntervals[0]
        mergedIntervals = [currentInterval]

        for nextInterval in sortedIntervals:
            if currentInterval[1] >= nextInterval[0]:
                currentInterval[1] = max(currentInterval[1], nextInterval[1])
            else:
                currentInterval = nextInterval
                mergedIntervals.append(currentInterval)
        return mergedIntervals


# Unit Tests
funcs = [Solution().merge]


class TestMerge(unittest.TestCase):
    def testMerge1(self):
        for func in funcs:
            intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
            self.assertEqual(
                func(intervals=intervals), [[1, 6], [8, 10], [15, 18]]
            )

    def testMerge2(self):
        for func in funcs:
            intervals = [[1, 4], [4, 5]]
            self.assertEqual(
                func(intervals=intervals), [[1, 5]]
            )


if __name__ == "__main__":
    unittest.main()
