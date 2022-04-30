"""
493. Reverse Pairs
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

Example1:
Input: nums = [1,3,2,3,1]
Output: 2

Example2:
Input: nums = [2,4,3,5,1]
Output: 3

Constraints:
1 <= nums.length <= 5 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""

"""
Note 
1. Merge Sort: O(nlogn) time | O(nlogn) space
"""
from typing import List
class Solution(object):
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        result = [0] * n
        nums = [(n, i) for i, n in enumerate(nums)]

        def mergeTwoArray(leftArr, rightArr):
            n, m = len(leftArr), len(rightArr)
            i = j = rightCounter = 0
            while i < n and j < m:
                leftNum, leftIndex = leftArr[i]
                rightNum, _ = rightArr[j]
                if leftNum > rightNum * 2:
                    rightCounter += 1
                    j += 1
                else:
                    result[leftIndex] += rightCounter
                    i += 1
            
            while i < n:
                _, leftIndex = leftArr[i]
                result[leftIndex] += rightCounter
                i += 1
            
            # merge leftArr and rightArr into a sorted arr
            arr = []
            i = j = 0
            while i < n and j < m:
                if leftArr[i] <= rightArr[j]:
                    arr.append(leftArr[i])
                    i += 1
                else:
                    arr.append(rightArr[j])
                    j += 1
            arr.extend(leftArr[i:]) if i < n else arr.extend(rightArr[j:])
            return arr
        
        def reversePairsHelper(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            leftArr = reversePairsHelper(nums[:mid])
            rightArr = reversePairsHelper(nums[mid:])
            return mergeTwoArray(leftArr, rightArr)
        
        reversePairsHelper(nums)
        return sum(result)

# Unit Tests
import unittest
funcs = [Solution().reversePairs]

class TestReversePairs(unittest.TestCase):
    def testReversePairs1(self):
        for func in funcs:
            nums = [1,3,2,3,1]
            self.assertEqual(func(nums=nums), 2)

    def testReversePairs2(self):
        for func in funcs:
            nums = [2,4,3,5,1]
            self.assertEqual(func(nums=nums), 3)

if __name__ == "__main__":
    unittest.main()
