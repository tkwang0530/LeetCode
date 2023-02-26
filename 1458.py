"""
1458. Max Dot Product of Two Subsequences
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

Example1:
Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.

Example2:
Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.

Example3:
Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.

Constraints:
1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000
"""

"""
Note:
1. dfs+memo: O(mn) time | O(mn) space - where n is the length of array nums1 and m is the length of array nums2
"""




import unittest
from typing import List
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        maxLenOneProduct = float("-inf")
        for num1 in nums1:
            for num2 in nums2:
                maxLenOneProduct = max(maxLenOneProduct, num1*num2)
                if maxLenOneProduct > 0:
                    break

        if maxLenOneProduct < 0:
            return maxLenOneProduct

        memo = {}

        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            maxVal = max(
                dfs(i+1, j),
                dfs(i, j+1),
                dfs(i+1, j+1)+nums1[i] *
                nums2[j] if nums1[i]*nums2[j] > 0 else 0,
            )

            memo[(i, j)] = maxVal
            return memo[(i, j)]

        return dfs(0, 0)


# Unit Tests
funcs = [Solution().maxDotProduct]


class TestMaxDotProduct(unittest.TestCase):
    def testMaxDotProduct1(self):
        for func in funcs:
            nums1 = [2, 1, -2, 5]
            nums2 = [3, 0, -6]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 18)

    def testMaxDotProduct2(self):
        for func in funcs:
            nums1 = [3, -2]
            nums2 = [2, -6, 7]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 21)

    def testMaxDotProduct3(self):
        for func in funcs:
            nums1 = [-1, -1]
            nums2 = [1, 1]
            self.assertEqual(func(nums1=nums1, nums2=nums2), -1)


if __name__ == "__main__":
    unittest.main()
