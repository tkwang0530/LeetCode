"""
42. Trapping Rain Water
description: https://leetcode.com/problems/trapping-rain-water/description/
"""

"""
Note:
1. prefixMax + suffixMax: O(n) time | O(n) space - where n is the length of array height

2. Two Pointers: O(n) time | O(1) space
ref: https://www.youtube.com/watch?v=ZI2z5pq0TqA
"""

from typing import List
import unittest
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * (n+1)
        maxRight = [0] * (n+1)

        for i in range(1, n+1):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])

        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])

        water = 0
        for i in range(n):
            water += max(0, min(maxLeft[i], maxRight[i]) - height[i])

        return water

class Solution2:
    def trap(self, height: List[int]) -> int:
        maxLeft = maxRight = water = 0
        left, right = 0, len(height) - 1
        while left <= right:
            # move left to left + 1
            if maxLeft <= maxRight:
                water += max(0, min(maxLeft, maxRight)-height[left])
                maxLeft = max(maxLeft, height[left])
                left += 1
            else: # move right to right - 1
                water += max(0, min(maxLeft, maxRight)-height[right])
                maxRight = max(maxRight, height[right])
                right -= 1
        return water


# Unit Tests
funcs = [Solution().trap, Solution2().trap]


class TestTrap(unittest.TestCase):
    def testTrap1(self):
        for func in funcs:
            height = [0,1,0,2,1,0,1,3,2,1,2,1]
            self.assertEqual(func(height=height), 6)

    def testTrap2(self):
        for func in funcs:
            height = [4,2,0,3,2,5]
            self.assertEqual(func(height=height), 9)

if __name__ == "__main__":
    unittest.main()
