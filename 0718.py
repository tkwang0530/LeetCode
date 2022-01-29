"""
718. Maximum Length of Repeated Subarray
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
"""

""" 
1. LCS: O(mn) time | O(mn) space
"""

from typing import List
class Solution(object):
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) > len(nums1):
            nums2, nums1 = nums1, nums2
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        maxLength = 0
        for row in range(1, len(nums1)+1):
            for col in range(1, len(nums2)+1):
                num1 = nums1[row-1]
                num2 = nums2[col-1]
                if num1 == num2:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = 0
                maxLength = max(maxLength, dp[row][col])
        return maxLength


# Unit Tests
import unittest
funcs = [Solution().findLength]

class TestFindLength(unittest.TestCase):
    def testFindLength1(self):
        for func in funcs:
            nums1 = [1,2,3,2,1]
            nums2 = [3,2,1,4,7]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 3)

    def testFindLength2(self):
        for func in funcs:
            nums1 = [0,0,0,0,0]
            nums2 = [0,0,0,0,0]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 5)

if __name__ == "__main__":
    unittest.main()
