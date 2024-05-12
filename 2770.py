"""
2770. Maximum Number of Jumps to Reach the Last Index
description: https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/
"""

"""
Note:
1. dfs+memo: O(n^2) time | O(n^2) space - where n is the length of array nums
2 dp: O(n^2) time | O(n) space - where n is the length of array nums
"""

from typing import List
import functools
import unittest

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i):
            if i == n-1:
                return 0

            maxJumps = -float("inf")
            for j in range(i+1, n):
                if -target <= nums[j]-nums[i] <= target:
                    maxJumps = max(maxJumps, 1+dfs(j))
            
            return maxJumps
        return dfs(0) if dfs(0) != -float("inf") else -1

class Solution2:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [0] * n
        for i in range(n-2, -1, -1):
            maxJumps = -float("inf")
            for j in range(i+1, n):
                if -target <= nums[j]-nums[i] <= target:
                    maxJumps = max(maxJumps, 1+dp[j])
            dp[i] = maxJumps
        return dp[0] if dp[0] != -float("inf") else -1

# Unit Tests
funcs = [Solution().maximumJumps, Solution2().maximumJumps]
class TestMaximumJumps(unittest.TestCase):
    def testMaximumJumps1(self):
        for func in funcs:
            nums = [1,3,6,4,1,2]
            target = 2
            self.assertEqual(func(nums=nums, target=target), 3)

    def testMaximumJumps2(self):
        for func in funcs:
            nums = [1,3,6,4,1,2]
            target = 3
            self.assertEqual(func(nums=nums, target=target), 5)

    def testMaximumJumps3(self):
        for func in funcs:
            nums = [1,3,6,4,1,2]
            target = 0
            self.assertEqual(func(nums=nums, target=target), -1)




if __name__ == "__main__":
    unittest.main()