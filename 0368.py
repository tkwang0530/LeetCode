"""
368. Largest Divisible Subset
description: https://leetcode.com/problems/largest-divisible-subset/description/
"""

"""
Note:
1. dfs+sort: O(n^2) time | O(n^2) space - where n is the length of nums
2. dp+sort: O(n^2) time | O(n) space - where n is the length of nums
"""

import unittest
from typing import List
import collections
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        def dfs(i: int) -> List[int]:
            current = nums[i]
            if i == len(nums) - 1:
                newCandidates = collections.defaultdict(list)
                newCandidates[current] = [current]
                return newCandidates


            
            candidates = dfs(i+1)
            newCandidates = candidates.copy()
            for factor in candidates.keys():
                if factor % current == 0:
                    newCandidates[current] = max([current]+candidates[factor], newCandidates[current], key=len)
                    
            newCandidates[current] = max([current], newCandidates[current], key=len)
            return newCandidates

        maxGroup = []
        for _, group in dfs(0).items():
            if len(group) > len(maxGroup):
                maxGroup = group
        return list(maxGroup)
    
class Solution2:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        track = collections.defaultdict(lambda: -1)
        candidate = 0
        maxLen = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
                    track[i] = j
            if maxLen < dp[i]:
                maxLen = dp[i]
                candidate = i
        output = []
        while candidate >= 0:
            output.append(nums[candidate])
            candidate = track[candidate]

        return output

# Unit Tests
import unittest
funcs = [Solution().largestDivisibleSubset, Solution2().largestDivisibleSubset]
class TestLargestDivisibleSubset(unittest.TestCase):
    def testLargestDivisibleSubset1(self):
        for func in funcs:
            nums = [1,2,3]
            self.assertTrue(sorted(func(nums=nums)) == [1, 3] or sorted(func(nums=nums)) == [1, 2])

    def testLargestDivisibleSubset2(self):
        for func in funcs:
            nums = [1,2,4,8]
            self.assertEqual(sorted(func(nums=nums)), [1, 2, 4, 8])

if __name__ == "__main__":
    unittest.main()
