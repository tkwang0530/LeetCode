"""
2897. Apply Operations on Array to Maximize Sum of Squares
description: https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/description/
"""

"""
Note:
1. Greedy + bitwise: O(32n) time | O(32) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        n = len(nums)
        count = [0] * 32
        for i, num in enumerate(nums):
            for j in range(32):
                count[j] += num & 1
                num = num >> 1
                if num == 0:
                    break

        squareSums = 0
        for _ in range(k):
            num = 0
            for j in range(31, -1, -1):
                num = num << 1
                if count[j] > 0:
                    num += 1
                    count[j] -= 1
            if num == 0:
                break

            squareSums += num*num
        return squareSums % MOD

# Unit Tests
import unittest
funcs = [Solution().maxSum]

class TestMaxSum(unittest.TestCase):
    def testMaxSum1(self):
        for maxSum in funcs:
            nums = [2,6,5,8]
            k = 2
            self.assertEqual(maxSum(nums=nums, k=k), 261)

    def testMaxSum2(self):
        for maxSum in funcs:
            nums = [4,5,4,7]
            k = 3
            self.assertEqual(maxSum(nums=nums, k=k), 90)

if __name__ == "__main__":
    unittest.main()