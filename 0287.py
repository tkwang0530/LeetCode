"""
287. Find the Duplicate Number
description: https://leetcode.com/problems/find-the-duplicate-number/description/
"""

"""
Notes:
1. marker: O(n) time | O(1) space - where n is the length of nums
"""
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                return idx + 1
            nums[idx] *= -1
        return -1

# Unit Tests
import unittest
funcs = [Solution().findDuplicate]

class TestFindDuplicate(unittest.TestCase):
    def testFindDuplicate1(self):
        for func in funcs:
            nums = [1,3,4,2,2]
            self.assertEqual(func(nums=nums), 2)

    def testFindDuplicate2(self):
        for func in funcs:
            nums = [3,1,3,4,2]
            self.assertEqual(func(nums=nums), 3)

    def testFindDuplicate3(self):
        for func in funcs:
            nums = [3,3,3,3,3]
            self.assertEqual(func(nums=nums), 3)

if __name__ == "__main__":
    unittest.main()