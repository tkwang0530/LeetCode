"""
300. Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

For example, [3, 6, 2, 7] is a subsequence of the array [0, 3, 1, 6, 2, 2, 7]

Example1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4

Follow up: Can you come up with an algorithm that runs in O(nlogn) time complexity?
"""

"""
Note:
1. DP: O(n^2) time | O(n) space
2. DP + Binary Search: O(nlogn) time | O(n) space
tails is an array storing the smallest of all increasing subsequence with length i+1 in tails[i]
for example, say we have nums = [4, 5, 6, 3], then all the available increasing subsequences are:
len = 1: [4], [5], [6], [3] => tails[0] = 3
len = 2: [4, 5], [5, 6]      => tails[1] = 5
len = 3: [4, 5, 6]             => tails[2] = 6

We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.
Each time we only do one of the two:
(1) if num is larger than all tails, append it, increase the size by 1
(2) if tails[i-1] < num <= tails[i], update tails[i]
"""

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        n = len(nums)
        tails = [float("inf")] * (n+1) # tails[lengthOfSubsequence] = smallestTail
        tails[0] = -float("inf")
        maxSize = 0
        for num in nums:
            # bisect right
            left, right = 0, maxSize+1
            while left < right:
                mid = left + (right - left) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            # left will stop at the position where tails[left] >= num
            # which is also the next possible maxSize
            tails[left] = min(tails[left], num)
            maxSize = max(maxSize, left)
        return maxSize


# Unit Tests
import unittest
funcs = [Solution().lengthOfLIS, Solution().lengthOfLIS2]

class TestLengthOfLIS(unittest.TestCase):
    def testLengthOfLIS1(self):
        for func in funcs:
            nums = [10,9,2,5,3,7,101,18]
            self.assertEqual(func(nums=nums), 4)

    def testLengthOfLIS2(self):
        for func in funcs:
            nums = [0,1,0,3,2,3]
            self.assertEqual(func(nums=nums), 4)

    def testLengthOfLIS3(self):
        for func in funcs:
            nums = [7,7,7,7,7,7,7]
            self.assertEqual(func(nums=nums), 1)

if __name__ == "__main__":
    unittest.main()
