"""
350. Intersection of Two Arrays II
description: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
"""

"""
Note:
1. Hash Table (use one table): O(n+m) time | O(min(m, n)) space - where n is the length of nums1 and m is the length of nums2
Count how many times each number shows up
2. If already sorted use two pointers: O(n+m) time | O(1) space - where n is the length of nums1 and m is the length of nums2
3. Hash Table (use two tables): O(n+m) time | O(min(m,n)) space - where n is the length of nums1 and m is the length of nums2
coulde use list.extend([num for _ in range(count)]) for convenience
"""


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
    
    def intersect3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numCount1 = {}
        numCount2 = {}
        for num in nums1:
            numCount1[num] = numCount1.get(num, 0) + 1
        for num in nums2:
            numCount2[num] = numCount2.get(num, 0) + 1
            
        result = []
        for num in numCount1:
            count = min(numCount1[num], numCount2.get(num, 0))
            if count > 0:
                result.extend([num for _ in range(count)])
        return result

# Unit Tests
import unittest
funcs = [Solution().intersect, Solution().intersect2, Solution().intersect3]

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
