"""
974. Subarray Sums Divisible by K
description: https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
"""

""" 
Note:
1. HashMap: O(n) time | O(k) space - where n is the length of array nums and k is the input k
"""

from typing import List
import collections
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currentSum = 0
        remainderCounter = collections.defaultdict(int)
        remainderCounter[0] = 1
        divisibles = 0
        for num in nums:
            currentSum += num
            remainder = currentSum % k
            divisibles += remainderCounter[remainder]
            remainderCounter[remainder] += 1
        return divisibles

# Unit Tests
import unittest
funcs = [Solution().subarraysDivByK]

class TestSubarraysDivByK(unittest.TestCase):
    def testSubarraysDivByK1(self):
        for func in funcs:
            nums = [4,5,0,-2,-3,1]
            k = 5 
            self.assertEqual(func(nums=nums, k=k), 7)

    def testSubarraysDivByK2(self):
        for func in funcs:
            nums = [5]
            k = 9
            self.assertEqual(func(nums=nums, k=k), 0)


if __name__ == "__main__":
    unittest.main()
