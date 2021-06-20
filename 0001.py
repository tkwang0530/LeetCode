"""
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
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


class TestTwoSum(unittest.TestCase):
    def testTwoSum1(self):
        func = Solution().twoSum
        self.assertEqual(func(nums=[2, 7, 11, 15], target=9).sort(), [1, 0].sort())

    def testTwoSum2(self):
        func = Solution().twoSum
        self.assertEqual(func(nums=[3, 2, 4], target=6).sort(), [1, 2].sort())


if __name__ == "__main__":
    unittest.main()