"""
1851. Minimum Interval to Include Each Query
description: https://leetcode.com/problems/minimum-interval-to-include-each-query/description/
"""

"""
Note:
1. sweepLint + bst + hashTable: O((n+q)logn) time | O(n+q) space - where n is the length of array intervals, q is the length of array queries
"""
import collections
from typing import List
from sortedcontainers import SortedList
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        locSet = set()
        sweepLine = collections.defaultdict(list)
        for left, right in intervals:
            size = right-left+1
            sweepLine[left].append(size)
            sweepLine[right+1].append(-size)
            locSet.add(left)
            locSet.add(right+1)
        
        locOutputIndice = collections.defaultdict(list)
        for i, loc in enumerate(queries):
            locOutputIndice[loc].append(i)

        locSet |= set(queries)
        bst = SortedList()
        
        output = [-1] * len(queries)
        for loc in sorted(list(locSet)):
            for val in sweepLine[loc]:
                if val > 0:
                    bst.add(val)
                else:
                    bst.remove(-val)
            
            if bst:
                for outputIdx in locOutputIndice[loc]:
                    output[outputIdx] = bst[0]
        return output

# Unit Tests
import unittest
funcs = [Solution().minInterval]


class TestMinInterval(unittest.TestCase):
    def testMinInterval1(self):
        for func in funcs:
            intervals = [[1,4],[2,4],[3,6],[4,4]]
            queries = [2,3,4,5]
            self.assertEqual(func(intervals=intervals, queries=queries), [3,3,1,4])


    def testMinInterval2(self):
        for func in funcs:
            intervals = [[2,3],[2,5],[1,8],[20,25]]
            queries = [2,19,5,22]
            self.assertEqual(func(intervals=intervals, queries=queries), [2,-1,4,6])


if __name__ == "__main__":
    unittest.main()