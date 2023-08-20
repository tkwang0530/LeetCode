"""
1537. Get the Maximum Score
description: https://leetcode.com/problems/get-the-maximum-score/description/
"""

"""
Note:
1. dp: O(m+n) time | O(m+n) space - where m is the length of array nums1 and n is the length of array nums2
"""

from typing import List
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        M = 10 ** 9 + 7
        numSet1 = set(nums1)
        numSet2 = set(nums2)
        nums = sorted(list(set(nums1+nums2)))
        n = len(nums)
        grid = [[0]*(n+1) for _ in range(2)]
        
        k = 1
        for num in nums:
            if num in numSet1:
                grid[0][k] = num
            if num in numSet2:
                grid[1][k] = num
            k += 1
        
        dp = [[0]*(n+1) for _ in range(2)]

        for j in range(1, n+1):
            prevIsSame = grid[0][j-1] == grid[1][j-1]
            for i in range(2):
                if prevIsSame:
                    dp[i][j] = (grid[i][j] + max(dp[0][j-1], dp[1][j-1]))
                else:
                    dp[i][j] = (grid[i][j] + dp[i][j-1])
        return max(dp[0][-1], dp[1][-1]) % M


# Unit Tests
import unittest
funcs = [Solution().maxSum]
class TestMaxSum(unittest.TestCase):
    def testMaxSum1(self):
        for maxSum in funcs:
            nums1 = [2,4,5,8,10]
            nums2 = [4,6,8,9]
            self.assertEqual(maxSum(nums1=nums1, nums2=nums2), 30)

    def testMaxSum2(self):
        for maxSum in funcs:
            nums1 = [1,3,5,7,9]
            nums2 = [3,5,100]
            self.assertEqual(maxSum(nums1=nums1, nums2=nums2), 109)
    
    def testMaxSum3(self):
        for maxSum in funcs:
            nums1 = [1,2,3,4,5]
            nums2 = [6,7,8,9,10]
            self.assertEqual(maxSum(nums1=nums1, nums2=nums2), 40)

if __name__ == "__main__":
    unittest.main()
