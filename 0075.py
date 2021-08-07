"""
75. Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Example1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


Example2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example3:
Input: nums = [0]
Output: [0]

Example4:
Input: nums = [1]
Output: [1]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space
(1) Focus on 0 and 2: move 0 to the left, move 2 to the right, so that if there is 1, it must be in the middle
"""

import unittest
from  typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1
        while left < len(nums) - 1 and nums[left] == 0:
            left += 1
        while right > 0 and nums[right] == 2:
            right -= 1
        i = left
        while i <= right:
            if nums[i] == 2:
                self.swap(nums, i, right)
                right -= 1
            elif nums[i] == 0:
                self.swap(nums, i, left)
                left += 1
            i += 1

    def swap(self, nums: List[int], i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i] 

            

# Unit Tests
funcs = [Solution().sortColors]


class TestSortColors(unittest.TestCase):
    def testSortColors1(self):
        for func in funcs:
            nums = [2,0,2,1,1,0]
            func(nums=nums)
            self.assertEqual(
                nums, [0,0,1,1,2,2])

    def testSortColors2(self):
        for func in funcs:
            nums = [2,0,1]
            func(nums=nums)
            self.assertEqual(
                nums, [0,1,2])

    def testSortColors3(self):
        for func in funcs:
            nums = [0]
            func(nums=nums)
            self.assertEqual(
                nums, [0])

    def testSortColors4(self):
        for func in funcs:
            nums = [1]
            func(nums=nums)
            self.assertEqual(
                nums, [1])

if __name__ == "__main__":
    unittest.main()
