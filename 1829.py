"""
1829. Maximum XOR for Each Query
description: https://leetcode.com/problems/maximum-xor-for-each-query/description/ 
"""

"""
Note:
1. bit manipulation: O(n) time | O(n) space - where n is the length of array nums 
"""

from typing import List
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        XOR = nums[0]
        for i in range(1, n):
            XOR ^= nums[i]

        def invert(num, size):
            return ~num & ((1 << size) - 1)

        output = [0] * n
        for i in range(n):
            output[i] = invert(XOR, maximumBit)
            XOR ^= nums[n-i-1]
        return output

import unittest
funcs = [Solution().getMaximumXor]

class TestGetMaximumXor(unittest.TestCase):
    def testGetMaximumXor1(self):
        for func in funcs:
            nums = [0,1,1,3]
            maximumBit = 2
            self.assertEqual(func(nums=nums, maximumBit=maximumBit), [0,3,2,3])

    def testGetMaximumXor2(self):
        for func in funcs:
            nums = [2,3,4,7]
            maximumBit = 3
            self.assertEqual(func(nums=nums, maximumBit=maximumBit), [5,2,6,5])

    def testGetMaximumXor3(self):
        for func in funcs:
            nums = [0,1,2,2,5,7]
            maximumBit = 3
            self.assertEqual(func(nums=nums, maximumBit=maximumBit), [4,3,6,4,6,7])

if __name__ == "__main__":
    unittest.main()
