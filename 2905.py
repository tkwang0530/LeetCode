"""
2905. Find Indices With Index and Value Difference II
description: https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/
"""

"""
Note:
1. PreMin+PreMax: O(n) time | O(n) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        preMax = [(float("-inf"), -1)] * n
        preMin = [(float("inf"), -1)] * n


        preMax[0] = preMin[0] = (nums[0], 0)
        for i in range(1, n):
            preMax[i] = preMax[i-1]
            preMin[i] = preMin[i-1]
            if nums[i] > preMax[i][0]:
                preMax[i] = (nums[i], i)
            
            if nums[i] < preMin[i][0]:
                preMin[i] = (nums[i], i)

        for i in range(indexDifference, n):
            a = abs(nums[i] - preMax[i-indexDifference][0])
            b = abs(nums[i] - preMin[i-indexDifference][0])
            if a >= valueDifference:
                return [preMax[i-indexDifference][1], i]
            if b >= valueDifference:
                return [preMin[i-indexDifference][1], i]

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