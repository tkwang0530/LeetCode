"""
26. Remove Duplicates from Sorted Array
description: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""

"""
Note:
1. Two Pointer(index and i): O(n) time | O(1) space
"""

from typing import List
import unittest
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        preNum = None
        for num in nums:
            if num != preNum:
                nums[index] = num
                index += 1
                preNum = num
        return index



# Unit Tests
funcs = [Solution().removeDuplicates]


class TestRemoveDuplicates(unittest.TestCase):
    def testRemoveDuplicates1(self):
        for func in funcs:
            nums = [1,1,2]
            self.assertEqual(func(nums=nums), 2)
            self.assertEqual(nums[0:2], [1, 2])

    def testRemoveDuplicates2(self):
        for func in funcs:
            nums = [0,0,1,1,1,2,2,3,3,4]
            self.assertEqual(func(nums=nums), 5)
            self.assertEqual(nums[0:5], [0,1,2,3,4])

if __name__ == "__main__":
    unittest.main()
