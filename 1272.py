"""
1272. Remove Interval
A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).

You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.

Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.

Example1:
Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]

Example2:
Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]

Example3:
Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
Output: [[-5,-4],[-3,-2],[4,5],[8,9]]

Constraints:
1 <= intervals.length <= 10^4
-10^9 <= a_i < b_i <= 10^9
"""

"""
Note:
1. Sweep Line (Reverse): O(nlogn) time | O(n) space - where n is the length of array intervals
1. Update prev interval: O(n) time | O(n) space - where n is the length of array intervals
"""

import collections
from typing import List
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        sweep = collections.defaultdict(int)
        for start, end in intervals:
            sweep[start] += 1
            sweep[end] -= 1

        sweep[toBeRemoved[0]] -= 1
        sweep[toBeRemoved[1]] += 1

        updatedIntervals = []
        current = 0
        added = False
        for time in sorted(sweep.keys()):
            current += sweep[time]
            if current > 0 and current == sweep[time]:
                updatedIntervals.append([time, -1])
                added = True
            
            if current == 0 and added:
                updatedIntervals[-1][-1] = time
                added = False
        return updatedIntervals

    def removeInterval2(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        updatedIntervals = []
        for start, end in intervals:
            if start > toBeRemoved[1] or end < toBeRemoved[0]:
                updatedIntervals.append([start, end])
                continue

            if start < toBeRemoved[0]:
                updatedIntervals.append([start, toBeRemoved[0]])

            if end > toBeRemoved[1]:
                updatedIntervals.append([toBeRemoved[1], end])
        return updatedIntervals

# Unit Tests
import unittest
funcs = [Solution().removeInterval, Solution().removeInterval2]


class TestRemoveInterval(unittest.TestCase):
    def testRemoveInterval1(self):
        for func in funcs:
            intervals = [[0,2],[3,4],[5,7]]
            toBeRemoved = [1,6]
            self.assertEqual(func(intervals=intervals, toBeRemoved=toBeRemoved), [[0,1],[6,7]])

    def testRemoveInterval2(self):
        for func in funcs:
            intervals = [[0,5]]
            toBeRemoved = [2,3]
            self.assertEqual(func(intervals=intervals, toBeRemoved=toBeRemoved), [[0,2],[3,5]])

    def testRemoveInterval3(self):
        for func in funcs:
            intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]]
            toBeRemoved = [-1,4]
            self.assertEqual(func(intervals=intervals, toBeRemoved=toBeRemoved), [[-5,-4],[-3,-2],[4,5],[8,9]])


if __name__ == "__main__":
    unittest.main()
