"""
128. Longest Consecutive Sequence
description: https://leetcode.com/problems/longest-consecutive-sequence/description/
"""

"""
Notes:
1. HashTable: O(n) time | O(n) space - where n is the length of array nums
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        used = set()

        longest = 0
        for num in nums:
            if num in used:
                continue
            used.add(num)

            # extend right
            upper = num
            while upper+1 in numSet:
                used.add(upper+1)
                upper += 1
            
            # extend left
            lower = num
            while lower-1 in numSet:
                used.add(lower-1)
                lower -= 1
            
            longest = max(longest, upper-lower+1)
        return longest

# Unit Tests
import unittest
funcs = [Solution().longestConsecutive]

class TestLongestConsecutive(unittest.TestCase):
    def testLongestConsecutive1(self):
        for func in funcs:
            nums = [100,4,200,1,3,2]
            self.assertEqual(func(nums=nums), 4)

    def testLongestConsecutive2(self):
        for func in funcs:
            nums = [0,3,7,2,5,8,4,6,0,1]
            self.assertEqual(func(nums=nums), 9)

if __name__ == "__main__":
    unittest.main()