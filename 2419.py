"""
2419. Longest Subarray With Maximum Bitwise AND
You are given an integer array nums of size n.
Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
- In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.

Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.
A subarray is a consiguous sequence of elements within an array.

Example1:
Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.

Example2:
Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
"""

"""
Note:
1. Sliding Window: O(n) time | O(1) space - where n is the length of array nums
"""




from typing import List
import unittest
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxBitwiseAnd = max(nums)
        prev = -1
        count = maxCount = 0
        for num in nums:
            if num == prev:
                count += 1
            else:
                count = 1
                prev = num
            if num == maxBitwiseAnd:
                maxCount = max(maxCount, count)
        return maxCount


# Unit Tests
funcs = [Solution().longestSubarray]


class TestLongestSubarray(unittest.TestCase):
    def testLongestSubarray1(self):
        for func in funcs:
            nums = [1, 2, 3, 3, 2, 2]
            self.assertEqual(func(nums=nums), 2)

    def testLongestSubarray2(self):
        for func in funcs:
            nums = [1, 2, 3, 4]
            self.assertEqual(func(nums=nums), 1)


if __name__ == "__main__":
    unittest.main()
