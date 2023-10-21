"""
2903. Find Indices With Index and Value Difference I
description: https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/
"""

"""
Note:
1. Brute Force: O(n^2) time | O(n^2) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n  = len(nums)
        for i in range(n-indexDifference):
            for j in range(i+indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]

# Unit Tests
import unittest
funcs = [Solution().findIndices]

class TestFindIndices(unittest.TestCase):
    def testFindIndices1(self):
        for findIndices in funcs:
            nums = [5,1,4,1]
            indexDifference = 2
            valueDifference = 4
            self.assertEqual(findIndices(nums=nums, indexDifference=indexDifference, valueDifference=valueDifference), [0,3])

    def testFindIndices2(self):
        for findIndices in funcs:
            nums = [2,1]
            indexDifference = 0
            valueDifference = 0
            self.assertEqual(findIndices(nums=nums, indexDifference=indexDifference, valueDifference=valueDifference), [0,0])

    def testFindIndices3(self):
        for findIndices in funcs:
            nums = [1,2,3]
            indexDifference = 2
            valueDifference = 4
            self.assertEqual(findIndices(nums=nums, indexDifference=indexDifference, valueDifference=valueDifference), [-1,-1])

if __name__ == "__main__":
    unittest.main()