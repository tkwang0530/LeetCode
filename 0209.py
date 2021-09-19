"""
209. Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [nums1, nums2, ... ] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^9
1 <= nums[i] <= 10^5
"""

""" 
Notes:
1. Sliding Window: O(n) time | O(1) space - where n is the length of s
2. Binary Search: O(nlogn) time | O(1) space - where n is the length of s
"""

from typing import List
class Solution(object):
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = 0
        currentSum = 0
        minLength = float("inf")
        for end in range(len(nums)):
            currentSum += nums[end]
            while currentSum >= target and start <= end:
                minLength = min(minLength, end - start + 1)
                currentSum -= nums[start]
                start += 1
        return minLength if minLength <= len(nums) else 0
    
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        minLength = float("inf")
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        left = 0
        for right, num in enumerate(nums):
            if num >= target:
                left = self.findLeft(left, right, nums, target, num)
                minLength = min(minLength, right - left + 1)
        return minLength if minLength <= len(nums) else 0

    def findLeft(self, left, right, nums, target, num) -> int:
        while left < right:
            mid = left + (right - left) // 2
            if num - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left

# Unit Tests
import unittest
funcs = [Solution().minSubArrayLen, Solution().minSubArrayLen2]

class TestMinSubArrayLen(unittest.TestCase):
    def testMinSubArrayLen1(self):
        for func in funcs:
            target = 7
            nums = [2,3,1,2,4,3]
            self.assertEqual(func(target=target, nums=nums), 2)

    def testMinSubArrayLen2(self):
        for func in funcs:
            target = 4
            nums = [1,4,4]
            self.assertEqual(func(target=target, nums=nums), 1)

    def testMinSubArrayLen3(self):
        for func in funcs:
            target = 11
            nums = [1,1,1,1,1,1,1,1]
            self.assertEqual(func(target=target, nums=nums), 0)

if __name__ == "__main__":
    unittest.main()
