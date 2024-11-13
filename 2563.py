"""
2563. Count the Number of Fair Pairs
description: https://leetcode.com/problems/count-the-number-of-fair-pairs/description/ 
"""

"""
Note:
1. Sort + Binary Search: O(nlogn) time | O(1) space - where n is the length of array nums
"""

from typing import List
import bisect
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        fairs = 0
        for i in range(len(nums)):
            val = nums[i]
            L = bisect.bisect_left(nums, lower-val, i+1)
            R = bisect.bisect_right(nums, upper-val, i+1)
            if R-L > 0:
                fairs += R-L
        return fairs

import unittest
funcs = [Solution().countFairPairs]

class TestCountFairPairs(unittest.TestCase):
    def testCountFairPairs1(self):
        for func in funcs:
            nums = [0,1,7,4,4,5]
            lower = 3
            upper = 6
            self.assertEqual(func(nums=nums, lower=lower, upper=upper), 6)

    def testCountFairPairs2(self):
        for func in funcs:
            nums = [1,7,9,2,5]
            lower = 11
            upper = 11
            self.assertEqual(func(nums=nums, lower=lower, upper=upper), 1) 

if __name__ == "__main__":
    unittest.main()
