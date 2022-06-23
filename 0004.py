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
Determine i, j, such that a[0:i] + b[0:j] (exclusive) is the most small "after" numbers.
There could multiple pairs of such (i, j) if there are some duplicated numbers.
Each such pair satisfies the following criteria at the same time:
1. i + j == after
2. (j >= 1 and a[i] >= b[j-1]) or j == 0
3. (i>=1 and b[j] >= a[i-1]) or i == 0 
"""

from typing import List
class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = sorted((nums1, nums2), key=len)
        m, n = len(A), len(B)

        # if m+n == odd number (7), (m+n-1)//2 = 3
        # if m+n == even number (8), (m+n-1)//2 = 3
        after = (m+n-1) // 2 
        left, right = 0, m
        while left < right:
            i = left + (right - left) // 2
            j = after - i
            cond1 = (j >= 1 and A[i] >= B[j-1]) or j == 0
            cond2 = (i >= 1 and B[j] >= A[i-1]) or i == 0
            if cond1 and cond2:
                left = i
                break
            elif not cond1:
                left = i + 1
            else:
                right = i
        i = left
        j = after - i
        nextFew = sorted(A[i:i+2]+B[j:j+2])
        return (nextFew[0] + nextFew[1- (m+n)%2]) / 2.0

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
