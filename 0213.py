"""
213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example3:
Input: nums = [1,2,3]
Output: 3

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

"""
Notes:
1. DP: O(n) time | O(1) space
using the solution of House Robber as a function
"""

from typing import List

class Solution(object):
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.robHelper(nums, 0, len(nums) - 2), self.robHelper(nums, 1, len(nums) - 1))

    def robHelper(self, nums: List[int], start, end) -> int:
        last, now = 0, 0
        for i in range(start, end+1):
            last, now = now, max(last + nums[i], now)
        return now

# Unit Tests
import unittest
funcs = [Solution().rob]

class TestRob(unittest.TestCase):
    def testRob1(self):
        for func in funcs:
            nums = [2,3,2]
            self.assertEqual(func(nums=nums), 3)

    def testRob2(self):
        for func in funcs:
            nums = [1,2,3,1]
            self.assertEqual(func(nums=nums), 4)

    def testRob3(self):
        for func in funcs:
            nums = [1,2,3]
            self.assertEqual(func(nums=nums), 3)


if __name__ == "__main__":
    unittest.main()