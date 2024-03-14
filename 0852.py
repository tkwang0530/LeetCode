"""
852. Peak Index in a Mountain Array
description: https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
"""

""" 
1. binary Search: O(log(n)) time | O(1) space - where n is the length of A
"""
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr)-1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid-1]:
                right = mid
            else:
                left = mid+1
        return -1

# Unit Tests
import unittest
funcs = [Solution().peakIndexInMountainArray]


class TestPeakIndexInMountainArray(unittest.TestCase):
    def testPeakIndexInMountainArray1(self):
        for func in funcs:
            arr = [0,1,0]
            self.assertEqual(func(arr=arr), 1)

    def testPeakIndexInMountainArray2(self):
        for func in funcs:
            arr = [0,2,1,0]
            self.assertEqual(func(arr=arr), 1)

    def testPeakIndexInMountainArray3(self):
        for func in funcs:
            arr = [0,10,5,2]
            self.assertEqual(func(arr=arr), 1)

if __name__ == "__main__":
    unittest.main()
