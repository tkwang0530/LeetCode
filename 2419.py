"""
2419. Longest Subarray With Maximum Bitwise AND
description: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/
"""

"""
Note:
1. Sliding Window: O(n) time | O(1) space - where n is the length of array nums
2. One pass: O(n) time | O(1) space - where n is the length of array nums
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

class Solution2:
    def longestSubarray(self, nums: List[int]) -> int:
        maxNum = 0
        count = 0
        maxLength = 0
        for num in nums:
            if num < maxNum:
                count = 0
            elif num > maxNum:
                count = 1
                maxNum = num
                maxLength = 1
            else:
                count += 1
                maxLength = max(maxLength, count)

        return maxLength

# Unit Tests
funcs = [Solution().longestSubarray, Solution2().longestSubarray]


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
