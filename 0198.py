"""
198. House Robber
description: https://leetcode.com/problems/house-robber/description/
"""

"""
Notes:
1. DP (improved): O(n) time | O(1) space - where n is the length of nums
2. DP: O(n) time | O(n) space - where n is the length of nums
3. dfs+memo: O(n) time | O(n) space - where n is the length of nums
"""

import functools
from typing import List

class Solution(object):
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)
        return now

class Solution2:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        result = [0] * len(nums)
        result[0] = nums[0]
        result[1] = max(result[0], nums[1])
        for i in range(2, len(nums)):
            result[i] = max(result[i-1], result[i-2] + nums[i])
        return result[-1]

class Solution3:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i: int, isSafe: bool) -> int:
            if i == n:
                return 0

            maxAmount = 0
            # skip
            maxAmount = max(
                maxAmount, 
                dfs(i+1, True)
            )

            # rob if isSafe
            if isSafe:
                maxAmount = max(
                    maxAmount, 
                    nums[i] + dfs(i+1, False)
                )
            return maxAmount
        return dfs(0, True)

# Unit Tests
import unittest
funcs = [Solution().rob, Solution2().rob, Solution3().rob]

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