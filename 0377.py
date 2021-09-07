"""
377. Combination Sum IV
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

Example1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example2:
Input: nums = [9], target = 3
Output: 0

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
"""

"""
Note:
1. DFS: O(2^k) time | O(target) space
where k is the sum of (target / candidate)

2. DP (Recursion + Memorization): O(sum{target/num_i}) time | O(target) space
dp(nums, target): => all combinations that uses nums to sumup to target
    if target == 0: return {}
    return Union{{num_i} X dp(nums, target - num_i)} (num_i <= target)

3, DP(Iteration): O(target*nums) time | O(target) space
"""

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

    def combinationSum4_2(self, nums: List[int], target: int) -> int:
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

    def combinationSum4_3(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                times = dp[i-num] if i - num >= 0 else 0
                dp[i] += times
        return dp[target]


# Unit Tests
import unittest
funcs = [Solution().combinationSum4, Solution().combinationSum4_2, Solution().combinationSum4_3]


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
