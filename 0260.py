
"""
260. Single Number III
description: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/
"""

"""
Note:
1. bitwise XOR: O(n) time | O(1) space - where n is the length of the array nums
ref: https://www.youtube.com/watch?v=faoVORjd-T8
"""

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n

        diffBit = 1
        while not (diffBit & xor):
            diffBit <<= 1
        
        a = b = 0
        for n in nums:
            if diffBit & n:
                a ^= n
            else:
                b ^= n
        return [a, b]

# Unit Tests
import unittest
funcs = [Solution().singleNumber]

class TestSingleNumber(unittest.TestCase):
    def testSingleNumber1(self):
        for singleNumber in funcs:
            nums = [1,2,1,3,2,5]
            self.assertEqual(sorted(singleNumber(nums=nums)), sorted([3,5]))

    def testSingleNumber2(self):
        for singleNumber in funcs:
            nums = [-1,0]
            self.assertEqual(sorted(singleNumber(nums=nums)), sorted([-1,0]))

    def testSingleNumber3(self):
        for singleNumber in funcs:
            nums = [0,1]
            self.assertEqual(sorted(singleNumber(nums=nums)), sorted([0,1]))

if __name__ == "__main__":
    unittest.main()