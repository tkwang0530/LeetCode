"""
643. Minimum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

Example1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
n == nums.length
1 <= k <= n <= 10^5
-10^4 <= nums[i] <= 10^4
"""

""" 
1. Sliding Window: O(n) time | O(1) space
2. Prefix Sum: O(n) time | O(n) space
"""

from typing import List
class Solution(object):
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = maxSum = 0
        for i in range(k):
            currentSum += nums[i]
        
        if k == len(nums):
            return currentSum / k
        
        maxSum = currentSum
        for i in range(k, len(nums)):
            currentSum += nums[i]
            currentSum -= nums[i-k]
            maxSum = max(maxSum, currentSum)
        return maxSum / k

    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        prefixSums = [0] + nums
        for i in range(1, len(prefixSums)):
            prefixSums[i] += prefixSums[i-1]
        return max(prefixSums[i+k] - prefixSums[i] for i in range(len(prefixSums) - k)) / k

# Unit Tests
import unittest
funcs = [Solution().findMaxAverage, Solution().findMaxAverage2]
class TestFindMaxAverage(unittest.TestCase):
    def testFindMaxAverage1(self):
        for func in funcs:
            nums = [1,12,-5,-6,50,3]
            k = 4
            self.assertEqual(func(nums=nums, k=k), 12.75)

    def testFindMaxAverage2(self):
        for func in funcs:
            nums = [5]
            k = 1
            self.assertEqual(func(nums=nums, k=k), 5)

    def testFindMaxAverage3(self):
        for func in funcs:
            nums = [0, 1, 1, 3, 3]
            k = 4
            self.assertEqual(func(nums=nums, k=k), 2.0)

if __name__ == "__main__":
    unittest.main()
