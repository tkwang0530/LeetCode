"""
3097. Shortest Subarray With OR at Least K II
description: https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/description/
"""

"""
Note:
1. Sliding window: O(32 * n) time | O(32) space - where n is the length of nums
"""

import unittest
from typing import List
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bits = [0] * 32
        def convertToNum(bits):
            num = 0
            for power, bitCount in enumerate(bits):
                if bitCount > 0:
                    num += 2**power
            return num

        def bitwiseOR(bits, num):
            power = 0
            while num > 0:
                bit = num % 2
                if bit > 0:
                    bits[power] += 1
                num //= 2
                power += 1
            
        def bitwiseShrink(bits, num):
            power = 0
            while num > 0:
                bit = num % 2
                if bit > 0:
                    bits[power] -= 1
                num //= 2
                power += 1

        shortest = float("inf")
        start = 0
        for end in range(n):
            bitwiseOR(bits, nums[end])
            while start <= end and convertToNum(bits) >= k:
                shortest = min(shortest, end-start+1)
                bitwiseShrink(bits, nums[start])
                start += 1
        return shortest if shortest != float("inf") else -1

# Unit Tests
import unittest
funcs = [Solution().minimumSubarrayLength]
class TestMinimumSubarrayLength(unittest.TestCase):
    def testMinimumSubarrayLength1(self):
        for func in funcs:
            nums = [1,2,3]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 1)

    def testMinimumSubarrayLength2(self):
        for func in funcs:
            nums = [2,1,8]
            k = 10
            self.assertEqual(func(nums=nums, k=k), 3)

    def testMinimumSubarrayLength3(self):
        for func in funcs:
            nums = [1,2]
            k = 0
            self.assertEqual(func(nums=nums, k=k), 1)

if __name__ == "__main__":
    unittest.main()
