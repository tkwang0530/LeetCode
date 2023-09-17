"""
1569. Number of Ways to Reorder Array to Get Same BST
description: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/
"""

""" 
1. Math + Divide and Conquer: O(n^2) time | O(n^2) space - where n is the length of array nums
"""

import functools
from typing import List
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9+7

        @functools.lru_cache(None)
        def factorial(n):
          if n <= 1:
            return 1
          return factorial(n-1) * n

        @functools.lru_cache(None)
        def C(m, n):
            return factorial(m) // factorial(m-n) // factorial(n)

        def dfs(nums):
            if len(nums) <= 2:
                return 1
            
            root = nums[0]
            leftNums = []
            rightNums = []
            for num in nums:
                if num == root:
                    continue
                if num < root:
                    leftNums.append(num)
                else:
                    rightNums.append(num)

            leftRes = dfs(leftNums)
            rightRes = dfs(rightNums)

            n = len(leftNums)
            m = len(rightNums)
            return C(m+n, n) * leftRes * rightRes

        return dfs(nums) % mod - 1

# Unit Tests
import unittest
funcs = [Solution().numOfWays]


class TestNumOfWays(unittest.TestCase):
    def testNumOfWays1(self):
        for numOfWays in funcs:
            nums = [2,1,3]
            self.assertEqual(numOfWays(nums=nums), 1)

    def testNumOfWays2(self):
        for numOfWays in funcs:
            nums = [3,4,5,1,2]
            self.assertEqual(numOfWays(nums=nums), 5)

    def testNumOfWays3(self):
        for numOfWays in funcs:
            nums = [1,2,3]
            self.assertEqual(numOfWays(nums=nums), 0)

if __name__ == "__main__":
    unittest.main()
