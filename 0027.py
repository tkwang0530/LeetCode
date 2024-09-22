"""
27. Remove Element
description: https://leetcode.com/problems/remove-element/description/
"""
"""
Note:
1. Two Pointer(left and right): O(n) time | O(1) space
2. Two Pointer(index and i): O(n) time | O(1) space
"""


from typing import List
import unittest
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left

    def removeElement2(self, nums: List[int], val: int) -> int:
        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
        return index



# Unit Tests
funcs = [Solution().removeElement, Solution().removeElement2]


class TestRemoveElement(unittest.TestCase):
    def testRemoveElement1(self):
        for func in funcs:
            nums = [3,2,2,3]
            val = 3
            self.assertEqual(func(nums=nums, val=val), 2)
            self.assertEqual(sorted(nums[0:2]), sorted([2, 2]))

    def testRemoveElement2(self):
        for func in funcs:
            nums = [0,1,2,2,3,0,4,2]
            val = 2
            self.assertEqual(func(nums=nums, val=val), 5)
            self.assertEqual(sorted(nums[0:5]), sorted([0,1,4,0,3]))

if __name__ == "__main__":
    unittest.main()
