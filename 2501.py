"""
2501. Longest Square Streak in an Array
description: https://leetcode.com/problems/longest-square-streak-in-an-array/description/
"""

"""
Note:
1. Sort + HashSet: O(nlogn) time | O(n) space - where n is the length of array nums
"""

from typing import List
import unittest
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        numSet = set(nums)
        nums.sort()
        visited = set()
        
        maxLength = -1
        for num in nums:
            if num in visited:
                continue
            
            visited.add(num)
            runningLength = 1
            current = num
            while current**2 in numSet:
                visited.add(current**2)
                runningLength += 1
                current *= current


            if runningLength >= 2:
                maxLength = max(maxLength, runningLength)

        return maxLength

# Unit Tests
funcs = [Solution().longestSquareStreak]

class TestLongestSquareStreak(unittest.TestCase):
    def testLongestSquareStreak1(self):
        for func in funcs:
            nums = [4,3,6,16,8,2]
            self.assertEqual(func(nums=nums), 3)

    def testLongestSquareStreak2(self):
        for func in funcs:
            nums = [2,3,5,6,7]
            self.assertEqual(func(nums=nums), -1)

if __name__ == "__main__":
    unittest.main()
