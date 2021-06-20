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
"""

from typing import List


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


# Unit Tests
import unittest


class TestSingleNumber(unittest.TestCase):
    def testSingleNumber1(self):
        func = Solution().singleNumber
        self.assertEqual(func(nums=[2, 2, 1]), 1)

    def testSingleNumber2(self):
        func = Solution().singleNumber
        self.assertEqual(func(nums=[4, 1, 2, 1, 2]), 4)

    def testSingleNumber3(self):
        func = Solution().singleNumber
        self.assertEqual(func(nums=[1]), 1)

    def testSingleNumber4(self):
        func = Solution().singleNumber2
        self.assertEqual(func(nums=[2, 2, 1]), 1)

    def testSingleNumber5(self):
        func = Solution().singleNumber2
        self.assertEqual(func(nums=[4, 1, 2, 1, 2]), 4)

    def testSingleNumber6(self):
        func = Solution().singleNumber2
        self.assertEqual(func(nums=[1]), 1)


if __name__ == "__main__":
    unittest.main()