"""
368. Largest Divisible Subset
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]

Constraints:
1 <= nums.length <= 1000
"""

"""
Note:
1. dfs+sort: O(n^2) time | O(n^2) space
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

# Unit Tests
import unittest
funcs = [Solution().largestDivisibleSubset]
class TestLargestDivisibleSubset(unittest.TestCase):
    def testLargestDivisibleSubset1(self):
        for func in funcs:
            nums = [1,2,3]
            self.assertTrue(func(nums=nums) == [1, 3] or func(nums=nums) == [1, 2])

    def testLargestDivisibleSubset2(self):
        for func in funcs:
            nums = [1,2,4,8]
            self.assertEqual(func(nums=nums), [1, 2, 4, 8])

if __name__ == "__main__":
    unittest.main()
