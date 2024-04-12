"""
81. Search in Rotated Sorted Array II
description: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
"""

"""
Note:
1. Binary Search: O(n) time | O(1) space
O(logn) time for average case
"""

from typing import List
import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[left]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] <= target <= nums[right-1]:
                    left = mid + 1
                else:
                    right = mid
            else:
                left += 1
        return False

# Unit Tests
funcs = [Solution().search]

class TestSearch(unittest.TestCase):
    def testSearch1(self):
        for func in funcs:
            nums = [2,5,6,0,0,1,2]
            target = 0
            self.assertEqual(
                func(nums=nums, target=target), True)
    
    def testSearch2(self):
        for func in funcs:
            nums = [2,5,6,0,0,1,2]
            target = 3
            self.assertEqual(
                func(nums=nums, target=target), False)

if __name__ == "__main__":
    unittest.main()
