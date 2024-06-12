"""
75. Sort Colors
description: https://leetcode.com/problems/sort-colors/description/
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space
(1) Focus on 0 and 2: move 0 to the left, move 2 to the right, so that if there is 1, it must be in the middle

2. Count zero, one, two then reassign the value: O(n) time | O(1) space

3. Counting Sort: O(n) time | O(1) space
"""

import collections
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
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            else:
                i += 1

class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numCount = collections.Counter(nums)
        for i in range(len(nums)):
            if numCount[0]:
                nums[i] = 0
                numCount[0] -= 1
            elif numCount[1]:
                nums[i] = 1
                numCount[1] -= 1
            elif numCount[2]:
                nums[i] = 2
                numCount[2] -= 1

class Solution3:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numCounter = collections.Counter(nums)
        idx = 0
        for num in range(3):
            nums[idx:idx+numCounter[num]] = [num] * numCounter[num]
            idx = idx+numCounter[num]

# Unit Tests
import unittest
funcs = [Solution().sortColors, Solution2().sortColors, Solution3().sortColors]
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
