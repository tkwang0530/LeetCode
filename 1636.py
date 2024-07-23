"""
1636. Sort Array by Increasing Frequency
description: https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
"""

"""
Note:
1. Sort: O(nlogn) time | O(n) space - where n is the length of array names
"""

import unittest, collections
from typing import List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        output = []
        numCount = [(num, counter[num]) for num in counter.keys()]
        numCount.sort(key=lambda x: (x[1], -x[0]))
        for num, count in numCount:
            output.extend([num]*count)
        return output

# Unit Tests
funcs = [Solution().frequencySort]


class TestFrequencySort(unittest.TestCase):
    def testFrequencySort1(self):
        for frequencySort in funcs:
            nums = [1,1,2,2,2,3]
            self.assertEqual(frequencySort(nums=nums), [3,1,1,2,2,2])

    def testFrequencySort2(self):
        for frequencySort in funcs:
            nums = [2,3,1,3,2]
            self.assertEqual(frequencySort(nums=nums), [1,3,3,2,2])

    def testFrequencySort3(self):
        for frequencySort in funcs:
            nums = [-1,1,-6,4,5,-6,1,4,1]
            self.assertEqual(frequencySort(nums=nums), [5,-1,4,4,-6,-6,1,1,1])

if __name__ == "__main__":
    unittest.main()
