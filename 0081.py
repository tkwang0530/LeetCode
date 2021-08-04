"""
81. Search in Rotated Sorted Array II
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:
1 <= nums.length <= 5000
-10^4 < nums[i] <= 10^4
All values of nums are unique
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
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
