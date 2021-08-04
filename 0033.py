"""
33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-10^4 < nums[i] <= 10^4
All values of nums are unique
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
"""

"""
Note:
1. Binary Search: O(logn) time | O(1) space
there are two cases:
case1: nums[mid] is larger than nums[left]
case2: nums[mid] is not larger than nums[left]
for case1: if nums[left] <= target <= nums[mid]: update right to mid, otherwise update left to mid + 1
for case2: if nums[mid] <= target <= nums[right-1]: update left to mid+1, otherwise update right to mid 
"""

from typing import List
import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right-1]:
                    left  = mid + 1
                else:
                    right = mid
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
