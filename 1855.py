"""
1855. Maximum Distance Between a Pair of Values
You are given two non-increasing 0-indexed integer arrays nums1 and nums2.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j].
The distance of the pair is j-1.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length

Example1:
Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2
Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).

Example2:
Input: nums1 = [2,2,2], nums2 = [10,10,1]
Output: 1
Explanation: The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).

Example3:
Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
Output: 2
Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).

Constraints:
1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 105
Both nums1 and nums2 are non-increasing.
"""

"""
Note:
1. Two Pointers: O(n+m) time | O(1) space - where n is the length of nums1 and m is the length of nums2
"""

from typing import List
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = maxDiff = 0
        while i < len(nums1) and j < len(nums2):
            if nums2[j] >= nums1[i]:
                maxDiff = max(maxDiff, j-i)
                j += 1
            else:
                i += 1
            if i > j:
                j += 1
        return maxDiff

# Unit Tests
import unittest
funcs = [Solution().maxDistance]

class TestMaxDistance(unittest.TestCase):
    def testMaxDistance1(self):
        for func in funcs:
            nums1 = [55,30,5,4,2]
            nums2 = [100,20,10,10,5]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 2)

    def testMaxDistance2(self):
        for func in funcs:
            nums1 = [2,2,2]
            nums2 = [10,10,1]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 1)

    def testMaxDistance3(self):
        for func in funcs:
            nums1 = [30,29,19,5]
            nums2 = [25,25,25,25,25]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 2)

if __name__ == "__main__":
    unittest.main()