"""
377. Combination Sum IV
description: https://leetcode.com/problems/combination-sum-iv/description/
"""

"""
Note:
1. DFS: O(2^k) time | O(target) space
where k is the sum of (target / candidate)

2. DP (Recursion + Memorization): O(sum{target/num_i}) time | O(target) space
dp(nums, target): => all combinations that uses nums to sumup to target
    if target == 0: return {}
    return Union{{num_i} X dp(nums, target - num_i)} (num_i <= target)

3. DP(Iteration): O(target*nums) time | O(target) space

4. DFS + memo: O(target*n) time | O(target) space
"""

import functools
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        result = [0]
        self.dfs(nums, target, result)
        return result[0]

    def dfs(self, nums, target, result) -> None:
        if target < 0:
            return
        elif target == 0:
            result[0] += 1
            return
        else:
            for i in range(0, len(nums)):
                self.dfs(nums, target - nums[i], result)

class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = [-1] * (target+1)
        cache[0] = 1
        return self.dp(nums, target, cache)

    def dp(self, nums: List[int], target: int, cache: List[int]) -> int:
        if target < 0:
            return 0
        if cache[target] != -1:
            return cache[target]
        result = 0
        for num in nums:
            result += self.dp(nums, target - num, cache)
        cache[target] = result
        return cache[target]

class Solution3:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                times = dp[i-num] if i - num >= 0 else 0
                dp[i] += times
        return dp[target]
    
class Solution4:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @functools.lru_cache(None)
        def dfs(target):
            if target == 0:
                return 1

            combinations = 0
            for i in range(len(nums)):
                if target-nums[i] >= 0:
                    combinations += dfs(target-nums[i])
            return combinations
        return dfs(target)


# Unit Tests
import unittest
funcs = [Solution().combinationSum4, Solution2().combinationSum4, Solution3().combinationSum4, Solution4().combinationSum4]


class TestCombinationSum(unittest.TestCase):
    def testCombinationSum1(self):
        for func in funcs:
            nums = [1,2,3]
            target = 4
            self.assertEqual(func(nums=nums, target=target), 7)

    def testCombinationSum2(self):
        for func in funcs:
            nums = [9]
            target = 3
            self.assertEqual(func(nums=nums, target=target), 0)


if __name__ == "__main__":
    unittest.main()
