"""
2401. Longest Nice Subarray
You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.

Example1:
Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.

Example2:
Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

"""
Note:
1. Sliding Window + Bitwise: O(n) time | O(1) space - where n is the length of array nums
"""




import unittest
from typing import List
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        mask = 0
        maxLen = 0
        for right in range(len(nums)):
            while mask & nums[right] > 0:
                mask ^= nums[left]
                left += 1
            mask |= nums[right]
            maxLen = max(maxLen, right-left+1)
        return maxLen


# Unit Tests
funcs = [Solution().longestNiceSubarray]


class TestLongestNiceSubarray(unittest.TestCase):
    def testLongestNiceSubarray1(self):
        for func in funcs:
            nums = [1, 3, 8, 48, 10]
            self.assertEqual(func(nums=nums), 3)

    def testLongestNiceSubarray2(self):
        for func in funcs:
            nums = [3, 1, 5, 11, 13]
            self.assertEqual(func(nums=nums), 1)


if __name__ == "__main__":
    unittest.main()
