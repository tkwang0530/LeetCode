"""
213. House Robber II
description: https://leetcode.com/problems/house-robber-ii/description/
"""

"""
Notes:
1. DP: O(n) time | O(1) space
using the solution of House Robber as a function
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
    
        def robHelper(start, end):
            dp = [0, 0]
            for i in range(start, end+1):
                money = nums[i]
                newDp = max(money+dp[0], dp[1])
                dp[0], dp[1] = dp[1], newDp
            return dp[1]
        
        return max(robHelper(0, n-2), robHelper(1, n-1))

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