"""
1509. Minimum Difference Between Largest and Smallest Value in Three Moves
description: https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/
"""

"""
Note:
1. Sort: O(nlogn) time | O(sort) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        left, right = 0, len(nums)-1
        minDiff = nums[right]-nums[left]
        for popLeftCount in range(4):
            popRightCount = 3-popLeftCount
            left = 0+popLeftCount
            right = len(nums)-1-popRightCount
            minDiff = min(minDiff, nums[right]-nums[left])
        return minDiff

# Unit Tests
import unittest
funcs = [Solution().minDifference]

class TestMinDifference(unittest.TestCase):
    def testMinDifference1(self):
        for minDifference in funcs:
            nums = [5,3,2,4]
            self.assertEqual(minDifference(nums=nums), 0)

    def testMinDifference2(self):
        for minDifference in funcs:
            nums = [1,5,0,10,14]
            self.assertEqual(minDifference(nums=nums), 1)

    def testMinDifference3(self):
        for minDifference in funcs:
            nums = [3,100,20]
            self.assertEqual(minDifference(nums=nums), 0)

if __name__ == "__main__":
    unittest.main()