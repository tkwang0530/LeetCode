"""
1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
description: https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/description/
"""

"""
Note:
1. HashTable: O(max(n,m)^2) time | O(max(n,m)^2) space - where n is the length of array nums1 and m is the length of array nums2
"""

import unittest, collections
from typing import List
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1SquareCounter = collections.defaultdict(int)
        nums2SquareCounter = collections.defaultdict(int)
        for num in nums1:
            nums1SquareCounter[num**2] += 1
        
        for num in nums2:
            nums2SquareCounter[num**2] += 1

        nums1MultipleCounter = collections.defaultdict(int)
        nums2MultipleCounter = collections.defaultdict(int)
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                nums1MultipleCounter[nums1[i]*nums1[j]] += 1

        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                nums2MultipleCounter[nums2[i]*nums2[j]] += 1

        triplets = 0
        for square, count in nums1SquareCounter.items():
            triplets += count *  nums2MultipleCounter[square]

        for square, count in nums2SquareCounter.items():
            triplets += count *  nums1MultipleCounter[square]

        return triplets

# Unit Tests
funcs = [Solution().numTriplets]


class TestNumTriplets(unittest.TestCase):
    def testNumTriplets1(self):
        for numTriplets in funcs:
            nums1 = [7,4]
            nums2 = [5,2,8,9]
            self.assertEqual(numTriplets(nums1=nums1, nums2=nums2), 1)

    def testNumTriplets2(self):
        for numTriplets in funcs:
            nums1 = [1,1]
            nums2 = [1,1,1]
            self.assertEqual(numTriplets(nums1=nums1, nums2=nums2), 9)

    def testNumTriplets3(self):
        for numTriplets in funcs:
            nums1 = [7,7,8,3]
            nums2 = [1,2,9,7]
            self.assertEqual(numTriplets(nums1=nums1, nums2=nums2), 2)


if __name__ == "__main__":
    unittest.main()
