"""
2134. Minimum Swaps to Group All 1's Together II
description: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/
"""

"""
Note:
1. Sliding Window: O(n) time | O(1) space - where n is the length of array nums
"""

import unittest
from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = sum(nums)
        
        left = 0
        right = left+ones-1
        runningOnes = sum(nums[:ones])
        minSwaps = ones-runningOnes
        for left in range(1, n):
            right = (left+ones-1) % n
            runningOnes += nums[right] == 1
            runningOnes -= nums[left-1] == 1
            minSwaps = min(minSwaps, ones-runningOnes)
        return minSwaps

# Unit Tests
funcs = [Solution().minSwaps]

class TestMinSwaps(unittest.TestCase):
    def testMinSwaps1(self):
        for func in funcs:
            nums = [0,1,0,1,1,0,0]
            self.assertEqual(func(nums=nums), 1)

    def testMinSwaps2(self):
        for func in funcs:
            nums = [0,1,1,1,0,0,1,1,0]
            self.assertEqual(func(nums=nums), 2)

    def testMinSwaps3(self):
        for func in funcs:
            nums = [1,1,0,0,1]
            self.assertEqual(func(nums=nums), 0)

if __name__ == "__main__":
    unittest.main()
