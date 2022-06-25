"""
665. Non-decreasing Array
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i+1] holds for every i (0-based)
such that (0 <= i <= n-2)

Example1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:
n == nums.length
1 <= n <=10^4
-10^5 <= nums[i] <= 10^5
"""

"""
Note:
1. Array: O(n) time | O(1) space - where n is the length of array nums
"""
from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                count += 1
                if i >= 2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
        return count <= 1

# Unit Tests
import unittest
funcs = [Solution().checkPossibility]
class TestCheckPossibility(unittest.TestCase):
    def testCheckPossibility1(self):
        for func in funcs:
            nums = [4,2,3]
            self.assertEqual(func(nums=nums), True)

    def testCheckPossibility2(self):
        for func in funcs:
            nums = [4,2,1]
            self.assertEqual(func(nums=nums), False)

    def testCheckPossibility3(self):
        for func in funcs:
            nums = [3,4,2,3]
            self.assertEqual(func(nums=nums), False)

    def testCheckPossibility4(self):
        for func in funcs:
            nums = [-1,4,2,3]
            self.assertEqual(func(nums=nums), True)

    def testCheckPossibility5(self):
        for func in funcs:
            nums = [5,7,1,8]
            self.assertEqual(func(nums=nums), True)


if __name__ == "__main__":
    unittest.main()
