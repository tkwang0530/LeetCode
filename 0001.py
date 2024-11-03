"""
1. Two Sum
description: https://leetcode.com/problems/two-sum/description/
"""

from typing import List
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [i, dict[target - num]]
            else:
                dict[num] = i
        return


# Unit Tests
import unittest
funcs = [Solution().twoSum]

class TestTwoSum(unittest.TestCase):
    def testTwoSum1(self):
        for func in funcs:
            self.assertEqual(sorted(func(nums=[2, 7, 11, 15], target=9)), sorted([1, 0]))

    def testTwoSum2(self):
        for func in funcs:
            self.assertEqual(sorted(func(nums=[3, 2, 4], target=6)), sorted([1, 2]))


if __name__ == "__main__":
    unittest.main()