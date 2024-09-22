"""
88. Merge Sorted Array
description: https://leetcode.com/problems/merge-sorted-array/description/
"""

"""
Note:
1. Two Pointers + backward traverse: O(m+n) time | O(1) space
"""




from typing import List
import unittest
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m+n-1
        idx1 = m-1
        idx2 = n-1
        while idx1 >= 0 or idx2 >= 0:
            val1 = nums1[idx1] if idx1 >= 0 else -float("inf")
            val2 = nums2[idx2] if idx2 >= 0 else -float("inf")
            if val1 >= val2:
                nums1[i] = val1
                idx1 -= 1
            else:
                nums1[i] = val2
                idx2 -= 1
            i -= 1

# Unit Tests
funcs = [Solution().merge]


class TestMerge(unittest.TestCase):
    def testMerge1(self):
        for func in funcs:
            nums1 = [1,2,3,0,0,0]
            m = 3
            nums2 = [2,5,6]
            n = 3
            func(nums1=nums1, m=m, nums2=nums2, n=n)
            self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def testMerge2(self):
        for func in funcs:
            nums1 = [1]
            m = 1
            nums2 = []
            n = 0
            func(nums1=nums1, m=m, nums2=nums2, n=n)
            self.assertEqual(nums1, [1])

    def testMerge3(self):
        for func in funcs:
            nums1 = [0]
            m = 0
            nums2 = [1]
            n = 1
            func(nums1=nums1, m=m, nums2=nums2, n=n)
            self.assertEqual(nums1, [1])

if __name__ == "__main__":
    unittest.main()
