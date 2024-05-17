"""
2149. Rearrange Array Elements by Sign
description: https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
"""

"""
Note:
1. Two Pointers: O(n) time | O(n) space - where n is the length of array nums
2. Two Pointers(2): O(n) time | O(n) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # getNextPositiveIdxAfter returns the next positive integer's index after i (exclusive)
        def getNextPositiveIdxAfter(i):
            for j in range(i+1, n):
                if nums[j] > 0:
                    return j
            return n

        # getNextNegativeIdxAfter returns the next negative integer's index after i (exclusive)
        def getNextNegativeIdxAfter(i):
            for j in range(i+1, n):
                if nums[j] < 0:
                    return j
            return n

        i = j = -1
        output = []
        while i < n or j < n:
            i = getNextPositiveIdxAfter(i)
            j = getNextNegativeIdxAfter(j)
            if i < n:
                output.append(nums[i])
            if j < n:
                output.append(nums[j])
        return output

class Solution2:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positiveIdx = 0
        negativeIdx = 1
        output = [0] * n
        for num in nums:
            if num > 0:
                output[positiveIdx] = num
                positiveIdx += 2
            else:
                output[negativeIdx] = num
                negativeIdx += 2
        return output

# Unit Tests
import unittest
funcs = [Solution().rearrangeArray, Solution2().rearrangeArray]

class TestRearrangeArray(unittest.TestCase):
    def testRearrangeArray1(self):
        for func in funcs:
            nums = [3,1,-2,-5,2,-4]
            self.assertEqual(func(nums=nums), [3,-2,1,-5,2,-4])

    def testRearrangeArray2(self):
        for func in funcs:
            nums = [-1,1]
            self.assertEqual(func(nums=nums), [1,-1])

if __name__ == "__main__":
    unittest.main()
