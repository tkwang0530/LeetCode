"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

(O: bar, X: water)
                    O
        OXXXOOXO
_OXOOXOOOOOO

Example1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""

"""
Note:
1. find Heighest point + track leftHighest and rightHighest: O(n) time | O(1) space
(1) find the highest point, because we can then use this point to calculate the water on its left and on its right (find its index)
(2) 0 - highestIdx, highestIdx - len(), compute the trap water from tart to center and from end to center
(3) track the left highest point's index, water += left highest height - current height
(4) track the right highest point's index, water += right highest height - current height

2. One pass (only track leftHighest and rightHighest): O(n) time | O(1) space
"""

from typing import List
import unittest
class Solution:
    def trap(self, height: List[int]) -> int:
        peakIdx = 0
        leftHighestIdx = 0
        rightHighestIdx = 0
        water = 0
        for i in range(len(height)):
            if height[i] > height[peakIdx]:
                peakIdx = i
        
        for i in range(peakIdx):
            if height[i] > height[leftHighestIdx]:
                leftHighestIdx = i
            else:
                water += height[leftHighestIdx] - height[i]
        
        for i in range(len(height) - 1, peakIdx, -1):
            if height[i] > height[rightHighestIdx]:
                rightHighestIdx = i
            else:
                water += height[rightHighestIdx] - height[i]
        
        return water

    def trap2(self, height: List[int]) -> int:
        leftHighest = rightHighest = water = 0
        left, right = 0, len(height) - 1
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > leftHighest:
                    leftHighest = height[left]
                else:
                    water += leftHighest - height[left]
                left += 1
            else:
                if height[right] > rightHighest:
                    rightHighest = height[right]
                else:
                    water += rightHighest - height[right]
                right -= 1
        return water


# Unit Tests
funcs = [Solution().trap, Solution().trap2]


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
