"""
3254. Find the Power of K-Size Subarrays I
description: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/
"""

"""
Note:
1. One Pass: O(n) time | O(n-k+1) space - where n is the length of array nums 
"""

from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        L = 0
        prev = nums[0]-1
        output = []
        for R in range(len(nums)):
            if prev != nums[R]-1:
                L = R
    
            if R >= k-1:
                output.append(-1 if R-L+1 < k else nums[R])

            L = max(L, R-k+1)
            prev = nums[R]
        return output

import unittest
funcs = [Solution().resultsArray]

class TestResultsArray(unittest.TestCase):
    def testResultsArray1(self):
        for func in funcs:
            nums = [1,2,3,4,3,2,5]
            k = 3
            self.assertEqual(func(nums=nums, k=k), [3,4,-1,-1,-1])

    def testResultsArray2(self):
        for func in funcs:
            nums = [2,2,2,2,2]
            k = 4
            self.assertEqual(func(nums=nums, k=k), [-1,-1]) 

    def testResultsArray3(self):
        for func in funcs:
            nums = [3,2,3,2,3,2]
            k = 2
            self.assertEqual(func(nums=nums, k=k), [-1,3,-1,3,-1]) 

if __name__ == "__main__":
    unittest.main()
