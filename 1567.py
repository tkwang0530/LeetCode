"""
1567. Maximum Length of Subarray With Positive Product
description: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/description/
"""

""" 
1. Sliding Window: O(n) time | O(1) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        start = currentNC = 0
        maxLen = 0
        firstNIdx = -1
        
        for end in range(len(nums)):
            if nums[end] == 0:
                start = end + 1
                currentNC = 0
                firstNIdx = -1
                continue
                
            if nums[end] < 0:
                if firstNIdx == -1:
                    firstNIdx = end
                currentNC += 1
            
            if currentNC % 2 == 0:
                maxLen = max(maxLen, end-start+1)
            else:
                # find the first negative number in the window
                # candidateLen = E - (firstNIdx + 1) + 1
                maxLen = max(maxLen, end-(firstNIdx+1)+1)
        return maxLen

# Unit Tests
import unittest
funcs = [Solution().getMaxLen]


class TestGetMaxLen(unittest.TestCase):
    def testGetMaxLen1(self):
        for getMaxLen in funcs:
            nums = [1,-2,-3,4]
            self.assertEqual(getMaxLen(nums=nums), 4)

    def testGetMaxLen2(self):
        for getMaxLen in funcs:
            nums = [0,1,-2,-3,-4]
            self.assertEqual(getMaxLen(nums=nums), 3)

    def testGetMaxLen3(self):
        for getMaxLen in funcs:
            nums = [-1,-2,-3,0,1]
            self.assertEqual(getMaxLen(nums=nums), 2)

if __name__ == "__main__":
    unittest.main()
