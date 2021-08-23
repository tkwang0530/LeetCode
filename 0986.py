"""
986. Interval List Intersections
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [start_i, end_i] and secondList[j] = [start_j, end_j]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists

A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3]

Example1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Example3:
Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []

Example4:
Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]

Constraints:
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= start_i < end_i <= 10^9
end_i < start_i+1
0 <= start_j < end_j <= 10^9
end_j < start_j+1
"""

"""
Note:
1. Two Pointers: O(n+m) time | O(n+m) space
(1) find start = max(firstList's head, secondList's head)
(2) find end = min(firstList's tail, secondList's tail)
(3) if start <= end, that is [start, end] is a closed interval, then we append [start , end] to result list
(4) move their pointers depending on their tail's value
"""

from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i = j = 0
        result = []
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                result.append([start, end])
            
            if firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1
        return result


# Unit Tests
import unittest
funcs = [Solution().intervalIntersection]

class TestIntervalIntersection(unittest.TestCase):
    def testIntervalIntersection1(self):
        for func in funcs:
            firstList = [[0,2],[5,10],[13,23],[24,25]]
            secondList = [[1,5],[8,12],[15,24],[25,26]]
            self.assertEqual(
                func(firstList=firstList, secondList=secondList), [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
            )


    def testIntervalIntersection2(self):
        for func in funcs:
            firstList = [[1,3],[5,9]]
            secondList = []
            self.assertEqual(func(firstList=firstList, secondList=secondList), [])

    def testIntervalIntersection3(self):
        for func in funcs:
            firstList = []
            secondList = [[4,8],[10,12]]
            self.assertEqual(func(firstList=firstList, secondList=secondList), [])

    def testIntervalIntersection4(self):
        for func in funcs:
            firstList = [[1,7]]
            secondList = [[3,10]]
            self.assertEqual(func(firstList=firstList, secondList=secondList), [[3, 7]])

if __name__ == "__main__":
    unittest.main()