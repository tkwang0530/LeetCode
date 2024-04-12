"""
153. Find Minimum in Rotated Sorted Array
description: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""

"""
Note:
1. Binary Search: O(logn) time | O(1) space - where n is the length of array nums
if nums[mid] >= nums[right]: search right, otherwise search left 
"""

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            minVal = min(minVal, nums[mid])
            if nums[mid] >= nums[right]:
                left = mid+1
            else:
                right = mid-1
        return minVal

# Unit Tests
import unittest
funcs = [Solution().findMin]

class TestFindMin(unittest.TestCase):
    def testFindMin1(self):
        for func in funcs:
            nums = [3,4,5,1,2]
            self.assertEqual(func(nums=nums), 1)
    
    def testFindMin2(self):
        for func in funcs:
            nums = [4,5,6,7,0,1,2]
            self.assertEqual(func(nums=nums), 0)

    def testFindMin3(self):
        for func in funcs:
            nums = [11,13,15,17]
            self.assertEqual(func(nums=nums), 11)

if __name__ == "__main__":
    unittest.main()
