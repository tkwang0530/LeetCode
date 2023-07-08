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
3. Binary Search: O(nlogn) time | O(n) space - where n is the length of s
"""
import bisect
from typing import List
class Solution(object):
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        n = len(nums)
        start = 0
        currentSum = 0
        minLength = n
        for end in range(n):
            currentSum += nums[end]
            
            # 達成最小滿足條件
            while start < end and currentSum - nums[start] >= target:
                currentSum -= nums[start]
                start += 1
            
            if currentSum >= target:
                minLength = min(minLength, end-start+1)
        return minLength
    
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

    def minSubArrayLen3(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        n = len(nums)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + nums[i-1]
        
        minLength = n
        for i in range(n):
            A = target+preSums[i]
            j = bisect.bisect_left(preSums, A)
            if 0 <= j < len(preSums):
                minLength = min(minLength, j-i)
            
        return minLength

# Unit Tests
import unittest
funcs = [Solution().minSubArrayLen, Solution().minSubArrayLen2, Solution().minSubArrayLen3]

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
