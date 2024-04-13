"""
3105. Longest Strictly Increasing or Strictly Decreasing Subarray
description: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/
"""

"""
Note:
1. two pass + sliding window: O(n) time | O(1) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        longestIncrease = 1
        longestDecrease = 1
        start = 0
        prev = -float("inf")

        # increase
        for end in range(n):
            if nums[end] <= prev:
                prev = nums[end]
                start = end
                continue
            prev = nums[end]
            longestIncrease = max(longestIncrease, end-start+1)

        # decrease
        prev = float("inf")
        start = 0
        for end in range(n):
            if nums[end] >= prev:
                prev = nums[end]
                start = end
                continue
            prev = nums[end]
            longestDecrease = max(longestDecrease, end-start+1)

        return max(longestIncrease, longestDecrease)

# Unit Tests
import unittest
funcs = [Solution().longestMonotonicSubarray]

class TestLongestMonotonicSubarray(unittest.TestCase):
    def testLongestMonotonicSubarray1(self):
        for func in funcs:
            nums = [1,4,3,3,2]
            self.assertEqual(func(nums=nums), 2)

    def testLongestMonotonicSubarray2(self):
        for func in funcs:
            nums = [3,3,3,3]
            self.assertEqual(func(nums=nums), 1)

    def testLongestMonotonicSubarray3(self):
        for func in funcs:
            nums = [3,2,1]
            self.assertEqual(func(nums=nums), 3)

if __name__ == "__main__":
    unittest.main()
