"""
945. Minimum Increment to Make Array Unique
description: https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
"""

"""
Note:
1. Greedy: O(nlogn) time | O(sort) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        currentLargest = -float("inf")
        moves = 0
        nums.sort()
        for num in nums:
            if num < currentLargest:
                moves += currentLargest-num+1
            elif num == currentLargest:
                moves += 1
            
            currentLargest = max(num, currentLargest+1)
        return moves

# Unit Tests
import unittest
funcs = [Solution().minIncrementForUnique]
class TestMinIncrementForUnique(unittest.TestCase):
    def testMinIncrementForUnique1(self):
        for func in funcs:
            nums = [1,2,2]
            self.assertEqual(func(nums), 1)


    def testMinIncrementForUnique2(self):
        for func in funcs:
            nums = [3,2,1,2,1,7]
            self.assertEqual(func(nums), 6)


if __name__ == "__main__":
    unittest.main()
