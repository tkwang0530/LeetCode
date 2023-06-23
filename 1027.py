"""
1027. Longest Arithmetic Subsequence
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:
- A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
- A sequence seq is arithmetic if seq[i+1] - seq[i] are all the same value (for 0 <= 1 < seq.length - 1)

Example1:
Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.

Example2:
Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].

Example3:
Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].

Constraints:
2 <= nums.length <= 1000
0 <= nums[i] <= 500
"""

"""
Note:
1. DP + Array: O(n^2) time | O(n^2) space - where n is the length of array nums
A[j] * 3 = A[i] + A[j] + A[k]
A[i] = A[j] * 2 - A[k]
"""

import unittest
from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[2] * n for _ in range(n)]
        indice = [-1] * 501
        longest = 2
        for i in range(n):
            for j in range(i+1, n):
                first = nums[i] * 2 - nums[j]
                if first < 0 or first > 500 or indice[first] == -1:
                    continue
                dp[i][j] = dp[indice[first]][i] + 1
                longest = max(longest, dp[i][j])
            indice[nums[i]] = i
        return longest

# Unit Tests
import unittest
funcs = [Solution().longestArithSeqLength]
class TestLongestArithSeqLength(unittest.TestCase):
    def testLongestArithSeqLength1(self):
        for func in funcs:
            nums = [3,6,9,12]
            self.assertEqual(func(nums=nums), 4)

    def testLongestArithSeqLength2(self):
        for func in funcs:
            nums = [9,4,7,2,10]
            self.assertEqual(func(nums=nums), 3)

    def testLongestArithSeqLength3(self):
        for func in funcs:
            nums = [20,1,15,3,10,5,8]
            self.assertEqual(func(nums=nums), 4)

if __name__ == "__main__":
    unittest.main()
