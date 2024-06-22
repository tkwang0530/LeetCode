"""
1248. Count Number of Nice Subarrays
description: https://leetcode.com/problems/count-number-of-nice-subarrays/description/
"""

"""
Note:
1. HashTable: O(n) time | O(n) space - where n is the length of array nums
"""




import unittest, collections
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddCounters = collections.defaultdict(int)
        oddCounters[0] = 1
        runningCount = 0
        nices = 0
        for num in nums:
            runningCount += num % 2
            nices += oddCounters[runningCount-k]
            oddCounters[runningCount] += 1
        return nices


# Unit Tests
funcs = [Solution().numberOfSubarrays]


class TestNumberOfSubarrays(unittest.TestCase):
    def testNumberOfSubarrays1(self):
        for func in funcs:
            nums = [1,1,2,1,1]
            k = 3
            self.assertEqual(func(nums, k), 2)

    def testNumberOfSubarrays2(self):
        for func in funcs:
            nums = [2,4,6]
            k = 1
            self.assertEqual(func(nums, k), 0)

    def testNumberOfSubarrays3(self):
        for func in funcs:
            nums = [2,2,2,1,2,2,1,2,2,2]
            k = 2
            self.assertEqual(func(nums, k), 16)

if __name__ == "__main__":
    unittest.main()
