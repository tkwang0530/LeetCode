"""
2997. Minimum Number of Operations to Make Array XOR Equal to K
description: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/
"""

"""
Note:
1. Counter: O(32n) time | O(32) space - where n is the length of array nums
"""

import unittest
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        bitCount = [0] * 32
        for num in nums:
            for i in range(32):
                bitCount[i] += ((1 << i) & num > 0)


        ops = 0
        for i in range(32):
            kBit = ((1 << i) & k > 0)
            if (kBit % 2) != (bitCount[i] % 2):
                ops += 1
        return ops

# Unit Tests
import unittest
funcs = [Solution().minOperations]
class TestMinOperations(unittest.TestCase):
    def testMinOperations1(self):
        for func in funcs:
            nums = [2,1,3,4]
            k = 1
            self.assertEqual(func(nums=nums, k=k), 2)

    def testMinOperations2(self):
        for func in funcs:
            nums = [2,0,2,0]
            k = 0
            self.assertEqual(func(nums=nums, k=k), 0)

if __name__ == "__main__":
    unittest.main()
