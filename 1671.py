"""
1671. Minimum Number of Removals to Make Mountain Array
description: https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/ 
"""

"""
Note:
1. LIS + LDS: O(n^2) time | O(n) space - where n is the length of array nums
ref: https://www.youtube.com/watch?v=Ys-q9qPpleY
"""

from typing import List
import unittest
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        

        LDS = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    LDS[i] = max(LDS[i], 1 + LDS[j])
        
        minRemovals = float("inf")
        for i in range(1, n-1):
            if LIS[i] > 1 and LDS[i] > 1:
                minRemovals = min(
                    minRemovals,
                    n - LIS[i] - LDS[i] + 1
                )
        return minRemovals

# Unit Tests
funcs = [Solution().minimumMountainRemovals]

class TestMinimumMoutainRemovals(unittest.TestCase):
    def testMinimumMoutainRemovals1(self):
        for func in funcs:
            nums = [1,3,1]
            self.assertEqual(func(nums=nums), 0)

    def testMinimumMoutainRemovals2(self):
        for func in funcs:
            nums = [2,1,1,5,6,2,3,1]
            self.assertEqual(func(nums=nums), 3)

if __name__ == "__main__":
    unittest.main()
