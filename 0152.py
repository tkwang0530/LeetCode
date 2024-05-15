"""
152. Maximum Product Subarray
description: https://leetcode.com/problems/maximum-product-subarray/description/
"""

"""
Note:
1. Greedy + PreSum concept: O(n) time | O(n) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        runningProduct = 1
        maxNegProduct = -float("inf")
        maxProduct = -float("inf")
        for num in nums:
            runningProduct *= num
            maxProduct = max(maxProduct, runningProduct)
            if runningProduct == 0:
                runningProduct = 1
                maxNegProduct = -float("inf")
                continue

            if runningProduct < 0:
                if maxNegProduct != -float("inf"):
                    maxProduct = max(maxProduct, runningProduct//maxNegProduct)
                maxNegProduct = max(maxNegProduct, runningProduct)
        return maxProduct


# Unit Tests
import unittest
funcs = [Solution().maxProduct]


class TestMaxProduct(unittest.TestCase):
    def testMaxProduct1(self):
        for func in funcs:
            nums = [2,-2,0.5,0.5 ,2, -12]
            self.assertEqual(func(nums), 24)

    def testMaxProduct2(self):
        for func in funcs:
            nums = [2,3,-2,4]
            self.assertEqual(func(nums), 6)

    def testMaxProduct3(self):
        for func in funcs:
            nums = [-2,0,-1]
            self.assertEqual(func(nums), 0)

if __name__ == "__main__":
    unittest.main()