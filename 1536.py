"""
1536. Minimum Swaps to Arrange a Binary Grid
description: https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/
"""

"""
Note:
1. Sort + Binary Search: O(n^2logn) time | O(n) space - where n is the length of grid
"""

from typing import List
import bisect
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def countSuffixZeros(row: int) -> int:
            zeroes = 0
            i = n - 1
            while i >= 0 and grid[row][i] == 0:
                zeroes += 1
                i -= 1
            return zeroes

        zeroesProp = []
        for row in range(n):
            zeroesProp.append([countSuffixZeros(row), row])

        steps = 0
        for row in range(n-1):
            zeroesProp.sort()
            require = n - 1 - row

            idx = bisect.bisect_left(zeroesProp, [require, -1])
            if idx == len(zeroesProp):
                return -1

            steps += zeroesProp[idx][1] - row
            pivot = zeroesProp[idx][1]
            for i in range(len(zeroesProp)):
                if zeroesProp[i][0] >= require:
                    zeroesProp[i][0] = require - 1
                if zeroesProp[i][1] < pivot:
                    zeroesProp[i][1] += 1
            zeroesProp = zeroesProp[:idx] + zeroesProp[idx+1:]
        return steps


# Unit Tests
import unittest
funcs = [Solution().minSwaps]
class TestMinSwaps(unittest.TestCase):
    def testMinSwaps1(self):
        for minSwaps in funcs:
            grid = [[0,0,1],[1,1,0],[1,0,0]]
            self.assertEqual(minSwaps(grid=grid), 3)

    def testMinSwaps2(self):
        for minSwaps in funcs:
            grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
            self.assertEqual(minSwaps(grid=grid), -1)

    def testMinSwaps3(self):
        for minSwaps in funcs:
            grid = [[1,0,0],[1,1,0],[1,1,1]]
            self.assertEqual(minSwaps(grid=grid), 0)

if __name__ == "__main__":
    unittest.main()
