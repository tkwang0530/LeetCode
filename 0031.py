"""
31. Next Permutation
description: https://leetcode.com/problems/next-permutation/description/
"""

"""
Notes:
1. Two Pointers: O(n) time | O(1) space
(1) find the first number which is less than it's right
(2) if the number doesn't exist, reverse the nums and return
(3) for right to left, find the index where its value is larger than small
(4) exchange the value of small and big
(5) reverse the numbers  after "small" index (from small+1 to len(nums) - 1)
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        def reversedFrom(idx):
            left, right = idx, n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        reversedFrom(i+1)


# Unit Tests
import unittest
funcs = [Solution().nextPermutation]

class TestNextPermutation(unittest.TestCase):
    def testNextPermutation1(self):
        for func in funcs:
            nums = [1,2,3]
            func(nums=nums)
            self.assertEqual(nums, [1, 3, 2])

    def testNextPermutation2(self):
        for func in funcs:
            nums = [3,2,1]
            func(nums=nums)
            self.assertEqual(nums, [1, 2, 3])

    def testNextPermutation3(self):
        for func in funcs:
            nums = [1,1,5]
            func(nums=nums)
            self.assertEqual(nums, [1, 5, 1])

    def testNextPermutation4(self):
        for func in funcs:
            nums = [1]
            func(nums=nums)
            self.assertEqual(nums, [1])


if __name__ == "__main__":
    unittest.main()