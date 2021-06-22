"""
283. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements

Note that you must do this in-place without making a copy of the array.

Example1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example2:
Input: nums = [0]
Output: [0]
"""

"""
Note:
1. Two pointers(Fast and Slow): O(n) time | O(1) space
"""




from typing import List
import unittest
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
            if nums[slow] != 0:
                slow += 1


# Unit Tests
funcs = [Solution().moveZeroes]


class TestMoveZeroes(unittest.TestCase):
    def testMoveZeroes1(self):
        for func in funcs:
            nums = [0, 1, 0, 3, 12]
            func(nums=nums)
            self.assertEqual(nums, [1, 3, 12, 0, 0])

    def testMoveZeroes2(self):
        for func in funcs:
            nums = [0]
            func(nums=nums)
            self.assertEqual(nums, [0])


if __name__ == "__main__":
    unittest.main()
