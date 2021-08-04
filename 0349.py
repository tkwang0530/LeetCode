"""
349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

"""
Note:
1. Binary Search: O(nlogn + mlogm) time | O(m+n) space (.sort() is Timsort for python)
2. Set and set operation: O(m+n) time | O(m+n) space
"""

from typing import List
import unittest

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()
        nums2.sort()
        for i in range(len(nums1)):
            if i > 0 and nums1[i] == nums1[i-1]:
                continue
            left, right = 0, len(nums2)
            while left < right:
                mid = left + (right - left) // 2
                if nums2[mid] == nums1[i]:
                    result.append(nums1[i])
                    break
                elif nums2[mid] > nums1[i]:
                    right = mid
                else:
                    left = mid + 1
        return result

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))



# Unit Tests
funcs = [Solution().intersection, Solution().intersection2]

class TestIntersection(unittest.TestCase):
    def testIntersection1(self):
        for func in funcs:
            nums1 = [1,2,2,1]
            nums2 = [2,2]
            self.assertEqual(
                sorted(func(nums1=nums1, nums2=nums2)), [2])
    
    def testIntersection2(self):
        for func in funcs:
            nums1 = [4,9,5]
            nums2 = [9,4,9,8,4]
            self.assertEqual(
                sorted(func(nums1=nums1, nums2=nums2)), [4, 9])

if __name__ == "__main__":
    unittest.main()
