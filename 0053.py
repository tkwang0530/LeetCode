"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example2:
Input: nums = [1]
Output: 1

Example3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 3 * 10^4
-10^5 <= nums[i] <= 10^5

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

"""
Note:
1. track currSum and maxSub + remove negative prefix: O(n) time | O(1) space
2. recursive version of sol1: O(n) time | O(n) space
3. calculate sum using sliding window for every subarray: O(n^2) time | O(1) space
"""

import unittest
from  typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(maxSub, currSum)
        return maxSub

    def maxSubArray2(self, nums: List[int]) -> int:
        result = [nums[0]] # [maxSub]
        self.helper(nums, 0, 0, result)
        return result[0]

    def helper(self, nums, i, currSum, result):
        if i == len(nums):
            return
        if currSum < 0:
            currSum = 0
        currSum += nums[i]
        result[0] = max(result[0], currSum)
        self.helper(nums, i+1, currSum, result)

    def maxSubArray3(self, nums: List[int]) -> int:
        maxSub = nums[0]
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                maxSub = max(maxSub, currSum)
        return maxSub


# Unit Tests
funcs = [Solution().maxSubArray, Solution().maxSubArray2,Solution().maxSubArray3]


class TestMaxSubArray(unittest.TestCase):
    def testMaxSubArray1(self):
        for func in funcs:
            nums = [-2,1,-3,4,-1,2,1,-5,4]
            self.assertEqual(func(nums=nums), 6)

    def testMaxSubArray2(self):
        for func in funcs:
            nums = [1]
            self.assertEqual(func(nums=nums), 1)

    def testMaxSubArray3(self):
        for func in funcs:
            nums = [5, 4, -1, 7, 8]
            self.assertEqual(func(nums=nums), 23)


if __name__ == "__main__":
    unittest.main()
