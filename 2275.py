"""
2275. Largest Combination With Bitwise AND Greater Than Zero
description: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/description/ 
"""

"""
Note:
1. bit manipulation: O(25n) time | O(1) space - where n is the length of array candidates
"""

from typing import List
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        largest = 0 
        for offset in range(24+1):
            bit = 1 << offset
            valids = 0
            for num in candidates:
                valids += (bit & num > 0)
            largest = max(largest, valids)
        return largest

# Unit Tests
import unittest
funcs = [Solution().largestCombination]

class TestLargestCombination(unittest.TestCase):
    def testLargestCombination1(self):
        for func in funcs:
            candidates = [16,17,71,62,12,24,14]
            self.assertEqual(func(candidates=candidates), 4)

    def testLargestCombination2(self):
        for func in funcs:
            candidates = [8,8]
            self.assertEqual(func(candidates=candidates), 2)

if __name__ == "__main__":
    unittest.main()
