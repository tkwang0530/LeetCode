"""
3107. Minimum Operations to Make Median of Array Equal to K
description: https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/description/
"""

"""
Note:
1. Sort: O(nlogn) time | O(sort) space - where n is the length of array nums
"""

from typing import List

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ops = 0

        for i, num in enumerate(nums):
            if i < n // 2:
                ops += max(num-k, 0)
            elif i > n // 2:
                ops += max(k-num, 0)
            else:
                ops += abs(k-num)
        return ops

# Unit Tests
import unittest
funcs = [Solution().minOperationsToMakeMedianK]

class TestMinOperationsToMakeMedianK(unittest.TestCase):
    def testMinOperationsToMakeMedianK1(self):
        for func in funcs:
            nums = [2,5,6,8,5]
            k = 4
            self.assertEqual(func(nums=nums, k=k), 2)

    def testMinOperationsToMakeMedianK2(self):
        for func in funcs:
            nums = [2,5,6,8,5]
            k = 7
            self.assertEqual(func(nums=nums, k=k), 3)

    def testMinOperationsToMakeMedianK3(self):
        for func in funcs:
            nums = [1,2,3,4,5,6]
            k = 4
            self.assertEqual(func(nums=nums, k=k), 0)


if __name__ == "__main__":
    unittest.main()
