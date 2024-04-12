"""
33. Search in Rotated Sorted Array
description: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""

"""
Note:
1. Binary Search: O(logn) time | O(1) space - where n is the length of array nums
"""

from typing import List
import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]: # left portion
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else: # right portion
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1


# Unit Tests
funcs = [Solution().search]

class TestSearch(unittest.TestCase):
    def testSearch1(self):
        for func in funcs:
            nums = [4,5,6,7,0,1,2]
            target = 0
            self.assertEqual(
                func(nums=nums, target=target), 4)
    
    def testSearch2(self):
        for func in funcs:
            nums = [4,5,6,7,0,1,2]
            target = 3
            self.assertEqual(
                func(nums=nums, target=target), -1)

    def testSearch3(self):
        for func in funcs:
            nums = [1]
            target = 0
            self.assertEqual(
                func(nums=nums, target=target), -1)

if __name__ == "__main__":
    unittest.main()
