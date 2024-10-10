"""
962. Maximum Width Ramp
description: https://leetcode.com/problems/maximum-width-ramp/description/
"""

"""
Note:
1. SuffixMax + Sliding Window: O(n) time | O(n) space - where n is the length of array nums 
ref: https://www.youtube.com/watch?v=3pTEJ1vzgSI
"""

from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        suffixMax = [0] * n
        suffixMax[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffixMax[i] = max(suffixMax[i+1], nums[i])
        
        L = 0
        maxWidth = 0
        for R in range(n):
            rightMax = suffixMax[R]
            while nums[L] > rightMax:
                L += 1
            maxWidth = max(maxWidth, R-L)

        return maxWidth

funcs = [Solution().maxWidthRamp]

import unittest
class TestMaxWidthRamp(unittest.TestCase):
    def testMaxWidthRamp1(self):
        for func in funcs:
            nums = [6,0,8,2,1,5]
            self.assertEqual(func(nums=nums), 4)

    def testMaxWidthRamp2(self):
        for func in funcs:
            nums = [9,8,1,0,1,9,4,0,4,1]
            self.assertEqual(func(nums=nums), 7)

if __name__ == "__main__":
    unittest.main()
