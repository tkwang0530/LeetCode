"""
2461. Maximum Sum of Distinct Subarrays With Length K
description: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
"""

"""
Note:
1. Sliding Window + HashSet: O(n) time | O(k) space - where n is the length of array nums 
"""

from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = 0
        runningSum = 0
        L = 0
        numSet = set()
        for R in range(len(nums)):
            num = nums[R]
            runningSum += num
            while num in numSet or R-L+1 > k:
                runningSum -= nums[L]
                numSet.remove(nums[L])
                L += 1
            
            numSet.add(nums[R])
            if R-L+1 == k:
                maxSum = max(maxSum, runningSum)

        return maxSum

import unittest
funcs = [Solution().maximumSubarraySum]

class TestMaximumSubarraySum(unittest.TestCase):
    def testMaximumSubarraySum1(self):
        for func in funcs:
            nums = [1,5,4,2,9,9,9]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 15)

    def testMaximumSubarraySum2(self):
        for func in funcs:
            nums = [4,4,4]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 0) 

if __name__ == "__main__":
    unittest.main()
