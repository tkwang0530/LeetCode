"""
1051. Height Checker
description: https://leetcode.com/problems/height-checker/description/
"""

"""
Note:
1. Sort + One Pass: O(nlogn) time | O(n) space
2. Counting Sort: O(n) time | O(n) space
"""

import unittest
from  typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count += 1
        return count

    def heightChecker2(self, heights: List[int]) -> int:
        heightFreq = {}
        for height in heights:
            heightFreq[height] = heightFreq.get(height, 0) + 1
        
        currHeight = count = 0
        for i in range(len(heights)):
            while heightFreq.get(currHeight, 0) == 0:
                currHeight += 1
            if currHeight != heights[i]:
                count += 1
            heightFreq[currHeight] -= 1
        return count


# Unit Tests
funcs = [Solution().heightChecker, Solution().heightChecker2]


class TestHeightChecker(unittest.TestCase):
    def testHeightChecker1(self):
        for func in funcs:
            heights = [1,1,4,2,1,3]
            self.assertEqual(func(heights=heights), 3)

    def testHeightChecker2(self):
        for func in funcs:
            heights = [5,1,2,3,4]
            self.assertEqual(func(heights=heights), 5)

    def testHeightChecker3(self):
        for func in funcs:
            heights = [1,2,3,4,5]
            self.assertEqual(func(heights=heights), 0)


if __name__ == "__main__":
    unittest.main()
