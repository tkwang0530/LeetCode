"""
1712. Ways to Split Array Into Three Subarrays
description: https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/description/
"""

"""
Note:
1. PreSum + Binary Search: O(nlogn) time | O(n) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + nums[i-1]
            
        def rangeSum(start, end): # rangeSum for index start to end-1 inclusive
            return preSums[end] - preSums[start]
        
        def condition(i, end):
            return rangeSum(i, end) <= rangeSum(end, n)

        def condition2(i, end):
            return rangeSum(0, i) <= rangeSum(i, end)

        def dfs(i):
            rightestSplit = -1
            leftestSplit = -1

            left, right = i+1, n
            while left < right:
                mid = left + (right-left) // 2
                if condition(i, mid):
                    rightestSplit = mid
                    left = mid + 1
                else:
                    right = mid
                    
            
            left1, right1 = i+1, n
            while left1 < right1:
                mid = left1 + (right1-left1) // 2
                if condition2(i, mid):
                    leftestSplit = mid
                    right1 = mid
                else:
                    left1 = mid+1

            if -1 in (leftestSplit, rightestSplit) or leftestSplit > rightestSplit:
                return 0

            return (rightestSplit-leftestSplit+1) % MOD
        
        ways = 0
        for i in range(1, n-1):
            ways += dfs(i)
            
        return ways % MOD

# Unit Tests
import unittest
funcs = [Solution().waysToSplit]
class TestWaysToSplit(unittest.TestCase):
    def testWaysToSplit1(self):
        for func in funcs:
            nums = [1,1,1]
            self.assertEqual(func(nums=nums), 1)

    def testWaysToSplit2(self):
        for func in funcs:
            nums = [1,2,2,2,5,0]
            self.assertEqual(func(nums=nums), 3)

    def testWaysToSplit3(self):
        for func in funcs:
            nums = [3,2,1]
            self.assertEqual(func(nums=nums), 0)

if __name__ == "__main__":
    unittest.main()
