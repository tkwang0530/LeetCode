"""
1710. Maximum Units on a Truck
description: https://leetcode.com/problems/maximum-units-on-a-truck/description/
"""

"""
Note:
1. Greedy: O(nlogn) time | O(sort) space - where n is the length of array boxTypes
"""

from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1])
        puttedUnits = 0
        idx = len(boxTypes) - 1
        while idx >= 0 and truckSize > 0:
            puttedBoxes = min(boxTypes[idx][0], truckSize)
            puttedUnits += puttedBoxes * boxTypes[idx][1]
            truckSize -= puttedBoxes
            idx -= 1
        return puttedUnits

# Unit Tests
import unittest
funcs = [Solution().maximumUnits]
class TestMaximumUnits(unittest.TestCase):
    def testMaximumUnits1(self):
        for func in funcs:
            boxTypes = [[1,3],[2,2],[3,1]]
            truckSize = 4
            self.assertEqual(func(boxTypes=boxTypes, truckSize=truckSize), 8)

    def testMaximumUnits2(self):
        for func in funcs:
            boxTypes = [[5,10],[2,5],[4,7],[3,9]]
            truckSize = 10
            self.assertEqual(func(boxTypes=boxTypes, truckSize=truckSize), 91)

if __name__ == "__main__":
    unittest.main()
