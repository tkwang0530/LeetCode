"""
2760. Longest Even Odd Subarray With Threshold 
description: https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/description
"""

"""
Note:
1. Sliding Window: O(n) time | O(1) space
"""

from typing import List
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
      n = len(nums)
        l = 0
        longest = 0
        
        while l < n:
            if nums[l] % 2 > 0 or nums[l] > threshold:
                l += 1
                continue
            
            r = l
            # shouldBe
            # shouldBeEven = 0
            # shouldBeOdd = 1
            shouldBe = 0
            while r < n and nums[r] % 2 == shouldBe and nums[r] <= threshold:
                longest = max(longest, r-l+1)
                r += 1
                shouldBe ^= 1
            
            l = r
        
        return longest

# Unit Tests
import unittest
funcs = [Solution().longestAlternatingSubarray]

class TestLongestAlternatingSubarray(unittest.TestCase):
    def testLongestAlternatingSubarray1(self):
        for func in funcs:
            nums = [3,2,5,4]
            threshold = 5
            self.assertEqual(func(nums=nums, threshold=threshold), 3)
    def testLongestAlternatingSubarray2(self):
        for func in funcs:
            nums = [1,2]
            threshold = 2
            self.assertEqual(func(nums=nums, threshold=threshold), 1)
     
    def testLongestAlternatingSubarray3(self):
        for func in funcs:
            nums = [2,3,4,5]
            threshold = 4
            self.assertEqual(func(nums=nums, threshold=threshold), 3)

if __name__ == "__main__":
    unittest.main()
