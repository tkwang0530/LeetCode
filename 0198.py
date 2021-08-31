"""
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

"""
Notes:
1. DP (improved): O(n) time | O(1) space
2. DP: O(n) time | O(n) space
"""

from typing import List

class Solution(object):
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)
        return now

    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        result = [0] * len(nums)
        result[0] = nums[0]
        result[1] = max(result[0], nums[1])
        for i in range(2, len(nums)):
            result[i] = max(result[i-1], result[i-2] + nums[i])
            print(result[i])
        return result[-1]

# Unit Tests
import unittest
funcs = [Solution().rob, Solution().rob2]

class TestRob(unittest.TestCase):
    def testRob1(self):
        for func in funcs:
            nums = [1,2,3,1]
            self.assertEqual(func(nums=nums), 4)

    def testRob2(self):
        for func in funcs:
            nums = [2,7,9,3,1]
            self.assertEqual(func(nums=nums), 12)


if __name__ == "__main__":
    unittest.main()