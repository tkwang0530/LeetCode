"""
136. Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example1:
Input: [2, 2, 1]
Output: 1

Example2:
Input: [4, 1, 2, 1, 2]
Output: 4
"""

"""
Note:
1. Hash Table: O(n) time | O(n) space
Store a (key, value) pair where key is num, value is how many times it showed up.

2. math: O(n) time | O(n) space
2 * (a+b+c) - (a + a + b + b + c) = c

3. Bit Manipulation (XOR): O(n) time | O(1) space
"""

from typing import List
from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        for num in map:
            if map[num] == 1:
                return num

    def singleNumber2(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber3(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x ^ y, nums)

# Unit Tests
funcs = [Solution().singleNumber, Solution().singleNumber2, Solution().singleNumber3]
import unittest

class TestSingleNumber(unittest.TestCase):
    def testSingleNumber1(self):
        for func in funcs:
            self.assertEqual(func(nums=[2, 2, 1]), 1)

    def testSingleNumber2(self):
        for func in funcs:
            self.assertEqual(func(nums=[4, 1, 2, 1, 2]), 4)

    def testSingleNumber3(self):
        for func in funcs:
            self.assertEqual(func(nums=[1]), 1)

if __name__ == "__main__":
    unittest.main()