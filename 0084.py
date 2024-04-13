"""
84. Largest Rectangle in Histogram
description: https://leetcode.com/problems/largest-rectangle-in-histogram/description/
"""

"""
Note:
1. monotonic stack: O(n) time | O(n) space - where n is the length of array heights
ref: https://www.youtube.com/watch?v=zx5Sw9130L0
"""

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # [(index, height)]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

# Unit Tests
import unittest
funcs = [Solution().largestRectangleArea]

class TestLargestRectangleArea(unittest.TestCase):
    def testLargestRectangleArea1(self):
        for func in funcs:
            heights = [2,1,5,6,2,3]
            self.assertEqual(func(heights=heights), 10)

    def testLargestRectangleArea2(self):
        for func in funcs:
            heights = [2,4]
            self.assertEqual(func(heights=heights), 4)

if __name__ == "__main__":
    unittest.main()
