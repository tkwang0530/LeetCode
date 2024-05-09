
"""
1031. Maximum Sum of Two Non-Overlapping Subarrays
description: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
"""

"""
Note:
1. prefixSum + dfs + memo: O(n) time | O(n) space - where n is the length of array nums
"""

from typing import List
import functools
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + nums[i-1]

        def rangeSum(i, j):
            return preSums[j+1] - preSums[i]

        @functools.lru_cache(None)
        def dfs(i, L1, L2):
            if L1 == 0 and L2 == 0:
                return 0
            
            if i == n:
                return -float("inf")

            maxSum = 0
            # skip
            maxSum = max(maxSum, dfs(i+1, L1, L2))

            # use L1 if enough len
            if L1 > 0 and i+L1 <= n:
                maxSum = max(maxSum, rangeSum(i, i+L1-1) + dfs(i+L1, 0, L2))
            
            # use L2 if enough len
            if L2 > 0 and i+L2 <= n:
                maxSum = max(maxSum, rangeSum(i, i+L2-1) + dfs(i+L2, L1, 0))
            
            return maxSum
        
        return dfs(0, firstLen, secondLen)

# Unit Tests
import unittest
funcs = [Solution().maxSumTwoNoOverlap]

class TestMaxSumTwoNoOverlap(unittest.TestCase):
    def testMaxSumTwoNoOverlap1(self):
        for maxSumTwoNoOverlap in funcs:
            nums = [0,6,5,2,2,5,1,9,4]
            firstLen = 1
            secondLen = 2
            self.assertEqual(maxSumTwoNoOverlap(nums=nums, firstLen=firstLen, secondLen=secondLen), 20)

    def testMaxSumTwoNoOverlap2(self):
        for maxSumTwoNoOverlap in funcs:
            nums = [3,8,1,3,2,1,8,9,0]
            firstLen = 3
            secondLen = 2
            self.assertEqual(maxSumTwoNoOverlap(nums=nums, firstLen=firstLen, secondLen=secondLen), 29)

    def testMaxSumTwoNoOverlap3(self):
        for maxSumTwoNoOverlap in funcs:
            nums = [2,1,5,6,0,9,5,0,3,8]
            firstLen = 4
            secondLen = 3
            self.assertEqual(maxSumTwoNoOverlap(nums=nums, firstLen=firstLen, secondLen=secondLen), 31)

if __name__ == "__main__":
    unittest.main()