"""
162. Find Peak Element
description: https://leetcode.com/problems/find-peak-element/description/
"""

"""
Note:
1. Binary Search: O(log(n)) time | O(1) space - where n is the length of nums
"""

from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left) // 2
            val = nums[mid]
            if (mid-1 < 0 or nums[mid-1] < val) and (mid+1 > len(nums)-1 or val > nums[mid+1]):
                return mid
            elif mid == 0 or nums[mid-1] > val:
                right = mid
            else:
                left = mid+1
            
        return left


# Unit Tests
import unittest
funcs = [Solution().findPeakElement]
class TestFindPeakElement(unittest.TestCase):
    def testFindPeakElement1(self):
        for func in funcs:
            nums = [1,2,3,1]
            self.assertEqual(func(nums=nums), 2)

    def testFindPeakElement2(self):
        for func in funcs:
            nums = [1,2,1,3,5,6,4]
            self.assertEqual(func(nums=nums), 5)

if __name__ == "__main__":
    unittest.main()
