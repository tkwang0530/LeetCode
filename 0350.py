"""
350. Intersection of Two Arrays II
Given two arrays, write a function to compute their intersection.

Example1:
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2, 2]

Example2:
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [4, 9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
"""

"""
Note:
1. Hash Table: O(n+m) time | O(min(m, n)) space
Count how many times each number shows up
2. If already sorted use two pointers
"""




import unittest
from typing import List
class Solution(object):
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        result = []
        for num in nums1:
            dict[num] = dict.get(num, 0) + 1
        for num in nums2:
            if num in dict and dict[num] > 0:
                dict[num] -= 1
                result.append(num)
        return result

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx1 = idx2 = 0
        result = []
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                result.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return result

        # Unit Tests
funcs = [Solution().intersect, Solution().intersect2]


class TestIntersect(unittest.TestCase):
    def testIntersect1(self):
        for func in funcs:
            nums1 = [1, 2, 2, 1]
            nums2 = [2, 2]
            self.assertEqual(
                func(nums1=nums1, nums2=nums2).sort(), [2, 2].sort())

    def testIntersect2(self):
        for func in funcs:
            nums1 = [4, 9, 5]
            nums2 = [9, 4, 9, 8, 4]
            self.assertEqual(
                func(nums1=nums1, nums2=nums2).sort(), [4, 9].sort())


if __name__ == "__main__":
    unittest.main()