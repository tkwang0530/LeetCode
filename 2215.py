"""
2215. Find the Difference of Two Arrays
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

Example2:
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

Constraints:
1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000
"""

"""
Note:
1. HashTable: O(n+m) time | O(n+m) space - where n is the length of array nums1 and m is the length of array nums2
"""




import unittest
from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numSet1 = set(nums1)
        numSet2 = set(nums2)
        answer = [set(), set()]
        for num in nums1:
            if num in numSet2:
                continue
            answer[0].add(num)

        for num in nums2:
            if num in numSet1:
                continue
            answer[1].add(num)

        return [list(currentSet) for currentSet in answer]


# Unit Tests
funcs = [Solution().findDifference]


class TestFindDifference(unittest.TestCase):
    def testFindDifference1(self):
        for func in funcs:
            nums1 = [1, 2, 3]
            nums2 = [2, 4, 6]
            self.assertEqual(func(nums1=nums1, nums2=nums2), [[1, 3], [4, 6]])

    def testFindDifference2(self):
        for func in funcs:
            nums1 = [1, 2, 3, 3]
            nums2 = [1, 1, 2, 2]
            self.assertEqual(func(nums1=nums1, nums2=nums2), [[3], []])


if __name__ == "__main__":
    unittest.main()
