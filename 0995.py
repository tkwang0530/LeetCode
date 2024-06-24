"""
995. Minimum Number of K Consecutive Bit Flips
description: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description/
"""

"""
Note:
1. Sliding Window: O(n) time | O(1) space - where n is the length of array nums
ref: https://www.youtube.com/watch?v=Fv3M9uO5ovU
"""

import unittest
from typing import List
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        currentWindowFlips = 0
        flips = 0
        for i in range(len(nums)):
            if i - k >= 0 and nums[i - k] == 2:
                currentWindowFlips -= 1

            if (nums[i] + currentWindowFlips) % 2 == 0:
                if i + k > len(nums):
                    return -1
                flips += 1
                currentWindowFlips += 1
                nums[i] = 2
        return flips

# Unit Tests
funcs = [Solution().minKBitFlips]

class TestMinKBitFlips(unittest.TestCase):
    def testMinKBitFlips1(self):
        for minKBitFlips in funcs:
            nums = [0,1,0]
            k = 1
            self.assertEqual(minKBitFlips(nums=nums, k=k), 2)

    def testMinKBitFlips2(self):
        for minKBitFlips in funcs:
            nums = [1,1,0]
            k = 2
            self.assertEqual(minKBitFlips(nums=nums, k=k), -1)

    def testMinKBitFlips3(self):
        for minKBitFlips in funcs:
            nums = [0,0,0,1,0,1,1,0]
            k = 3
            self.assertEqual(minKBitFlips(nums=nums, k=k), 3)


if __name__ == "__main__":
    unittest.main()
