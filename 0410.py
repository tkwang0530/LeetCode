"""
410. Split Array Largest Sum
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Example1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example2:
Input: nums = [1,2,3,4,5], m = 2
Output: 9

Example3:
Input: nums = [1,4,4], m = 3
Output: 4
"""

"""
Note:
1. DFS (bottom up) + memo: O(nm(n-m)) time | O(nm) space - where n is the length of array nums
TLE: 29/30

2. DFS (bottom up) + Binary Search + memo: O(nmlog(n-m)) time | O(nm) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + nums[i-1]
            
        memo = {}
        def dfs(i, m) -> int:
            
            if m == 1:
                return preSums[-1] - preSums[i]
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            result = float("inf")
            
            # n-j => the number of left numbers from nums start from j
            # because n-j needs to be greater or equal to new m (m-1)
            # n-j >= m-1 => j <= n-m+1
            for j in range(i+1, n-m+2):
                # subSum = sum of subarray from i (inclusive) to j (exclusive)
                subSum = preSums[j] - preSums[i]
                result = min(result, max(dfs(j, m-1), subSum))
            memo[(i, m)] = result
            return memo[(i, m)]
        
        return dfs(0, m)

    def splitArray2(self, nums: List[int], m: int) -> int:
        n = len(nums)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + nums[i-1]
            
        memo = {}
        def dfs(i, m) -> int:
            if m == 1:
                return preSums[-1] - preSums[i]
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            # n-j => the number of left numbers from nums start from j
            # because n-j needs to be greater or equal to new m (m-1)
            # n-j >= m-1 => j <= n-m+1
            result = float("inf")
            left, right = i+1, n-m+2
            while left < right:
                mid = left + (right - left) // 2
                subSum = preSums[mid] - preSums[i] # left part
                rightResult = dfs(mid, m-1) # right part
                result = min(result, max(subSum, rightResult))
                if subSum <= rightResult:
                    left = mid + 1
                else:
                    right = mid
            memo[(i, m)] = result
            return memo[(i, m)]
        return dfs(0, m)

# Unit Tests
import unittest
funcs = [Solution().splitArray, Solution().splitArray2]
class TestSplitArray(unittest.TestCase):
    def testSplitArray1(self):
        for func in funcs:
            nums = [7,2,5,10,8]
            m = 2
            self.assertEqual(func(nums=nums, m=m), 18)

    def testSplitArray2(self):
        for func in funcs:
            nums = [1,2,3,4,5]
            m = 2
            self.assertEqual(func(nums=nums, m=m), 9)

    def testSplitArray3(self):
        for func in funcs:
            nums = [1,4,4]
            m = 3
            self.assertEqual(func(nums=nums, m=m), 4)


if __name__ == "__main__":
    unittest.main()
