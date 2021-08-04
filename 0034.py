"""
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Example1:
Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]

Example2:
Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
"""

"""
Note:
1. Binary Search: O(logn) time | O(1) space
"""

from typing import List
import unittest

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstIndex = self.findFirstIndex(nums, 0, len(nums), target)
        if firstIndex == -1:
            return [-1, -1]
        lastIndex = self.findLastIndex(nums, firstIndex, len(nums), target)
        return [firstIndex, lastIndex]

    def findFirstIndex(self, nums, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left if left != len(nums) and nums[left] == target else -1

    def findLastIndex(self, nums, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left - 1 if nums[left-1] == target else -1
            



# Unit Tests
funcs = [Solution().searchRange]

class TestSearchRange(unittest.TestCase):
    def testSearchRange1(self):
        for func in funcs:
            nums = [5, 7, 7, 8, 8, 10]
            target = 8
            self.assertEqual(
                sorted(func(nums=nums, target=target)), [3, 4])
    
    def testSearchRange2(self):
        for func in funcs:
            nums = [5, 7, 7, 8, 8, 10]
            target = 6
            self.assertEqual(
                sorted(func(nums=nums, target=target)), [-1, -1])

    def testSearchRange3(self):
        for func in funcs:
            nums = []
            target = 0
            self.assertEqual(
                sorted(func(nums=nums, target=target)), [-1, -1])

if __name__ == "__main__":
    unittest.main()
