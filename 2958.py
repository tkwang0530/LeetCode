"""
2958. Length of Longest Subarray With at Most K Frequency
description: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description
"""

"""
Note:
1. Sliding Window + HashMap: O(n) time | O(n) space - where n is the length of array nums
"""

import collections
from typing import List
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        numIndice = collections.defaultdict(list)
        for i in range(n-1, -1, -1):
            num = nums[i]
            numIndice[num].append(i)
        
        start = longest = 0
        counter = collections.defaultdict(int)
        for end in range(n):
            num = nums[end]
            counter[num] += 1
            if counter[num] > k:
                nextStart = numIndice[num][-1] + 1
                while start < nextStart:
                    startNum = nums[start]
                    counter[startNum] -= 1
                    numIndice[startNum].pop()
                    start += 1
            longest = max(longest, end - start + 1)
        return longest

# Unit Tests
import unittest
funcs = [Solution().maxSubarrayLength]


class TestMaxSubarrayLength(unittest.TestCase):
    def testMaxSubarrayLength1(self):
        for func in funcs:
            nums = [1,2,3,1,2,3,1,2]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 6)

    def testMaxSubarrayLength2(self):
        for func in funcs:
            nums = [1,2,1,2,1,2,1,2]
            k = 1
            self.assertEqual(func(nums=nums, k=k), 2)

    def testMaxSubarrayLength3(self):
        for func in funcs:
            nums = [5,5,5,5,5,5,5]
            k = 4
            self.assertEqual(func(nums=nums, k=k), 4)

if __name__ == "__main__":
    unittest.main()
