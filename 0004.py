"""
4. Median of Two Sorted Arrays
description: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""

""" 
1. Binary Search: O(log(min(n+m))) time | O(1) space
ref: https://www.youtube.com/watch?v=KB9IcSCDQ9k&ab_channel=HuaHua
"""

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2: return self.findMedianSortedArrays(nums2, nums1)

        k = (n1 + n2 + 1) // 2
        left, right = 0, n1

        while left < right:
            m1 = left + (right - left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1
        
        m1 = left
        m2 = k - left

        c1 = max(
            float("-inf") if m1 <= 0 else nums1[m1-1],
            float("-inf") if m2 <= 0 else nums2[m2-1]
        )
        
        if (n1+n2) % 2 == 1:
            return c1

        c2 = min(
            float("inf") if m1 >= n1 else nums1[m1],
            float("inf") if m2 >= n2 else nums2[m2]
        )

        return (c1 + c2) * 0.5

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

    def testFindMedianSortedArrays6(self):
        for func in funcs:
            nums1 = [1,2]
            nums2 = [-1,3]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 1.5)

if __name__ == "__main__":
    unittest.main()
