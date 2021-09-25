"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example5:
Input: nums1 = [2], nums2 = []
Output: 2.00000

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""

""" 
1. Binary Search: O(log(min(n+m))) time | O(1) space
"""

from typing import List
class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) +len(nums2)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1
        while True:
            mid = left + (right - left) // 2 # mid is the index for A

             # half - (mid + 1) is the size of the partition of B, while j is the index of the right most index of that partition 
            j = half - (mid + 1) - 1
            ALeft = A[mid] if mid >= 0 else float("-inf")
            ARight = A[mid+1] if mid+1 < len(A) else float("inf")
            BLeft = B[j] if j >= 0 else float("-inf")
            BRight = B[j+1] if j+1 < len(B) else float("inf")

            # partition is correct
            if ALeft <= BRight and BLeft <= ARight:
                # odd
                if total % 2 == 1:
                    return min(ARight, BRight)
                # even
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                right = mid - 1
            else:
                left = mid + 1
            


# Unit Tests
import unittest
funcs = [Solution().findMedianSortedArrays]


class TestFindMedianSortedArrays(unittest.TestCase):
    def testFindMedianSortedArrays1(self):
        for func in funcs:
            nums1 = [1,3]
            nums2 = [2]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 2.0)

    def testFindMedianSortedArrays2(self):
        for func in funcs:
            nums1 = [1,2]
            nums2 = [3,4]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 2.5)

    def testFindMedianSortedArrays3(self):
        for func in funcs:
            nums1 = [0,0]
            nums2 = [0,0]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 0.0)

    def testFindMedianSortedArrays4(self):
        for func in funcs:
            nums1 = []
            nums2 = [1]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 1.0)

    def testFindMedianSortedArrays5(self):
        for func in funcs:
            nums1 = [2]
            nums2 = []
            self.assertEqual(func(nums1=nums1, nums2=nums2), 2.0)

if __name__ == "__main__":
    unittest.main()
