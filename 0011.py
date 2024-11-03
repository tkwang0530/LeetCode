"""
11. Container With Most Water
description: https://leetcode.com/problems/container-with-most-water/description/ 
"""

""" 
Note
1. Two Pointers: O(n) time | O(1) space - where n is the length of array height
"""

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height)-1
        while left < right:
            water = max(water, min(height[left], height[right]) * (right-left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return water

# Unit Tests
import unittest
funcs = [Solution().maxArea]

class TestMaxArea(unittest.TestCase):
    def testMaxArea1(self):
        for func in funcs:
            height = [1,8,6,2,5,4,8,3,7]
            self.assertEqual(func(height=height), 49)

    def testMaxArea2(self):
        for func in funcs:
            height = [1,1]
            self.assertEqual(func(height=height), 1)

if __name__ == "__main__":
    unittest.main()
