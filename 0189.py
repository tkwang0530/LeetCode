"""
189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 10^6
"""

""" 
1. reverses 3 times: O(n) time | O(1) space
"""

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        nums.reverse()
        
        def reverseRangeFrom(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverseRangeFrom(0, k-1)
        reverseRangeFrom(k,  len(nums) - 1)

# Unit Tests
import unittest
funcs = [Solution().rotate]


class TestRotate(unittest.TestCase):
    def testRotate1(self):
        for func in funcs:
            nums = [1,2,3,4,5,6,7]
            k = 3
            func(nums=nums, k=k)
            self.assertEqual(nums, [5,6,7,1,2,3,4])

    def testRotate2(self):
        for func in funcs:
            nums = [-1,-100,3,99]
            k = 2
            func(nums=nums, k=k)
            self.assertEqual(nums, [3,99,-1,-100])

if __name__ == "__main__":
    unittest.main()
