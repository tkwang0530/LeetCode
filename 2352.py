
"""
2352. Equal Row and Column Pairs
description: https://leetcode.com/problems/equal-row-and-column-pairs/description/
"""

"""
Note:
1. Counter: O(n^2) time | O(n^2) space - where n is the length of matrix
"""

from typing import List
import collections
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        equals = 0
        valsRowCount = collections.defaultdict(int)
        for row in range(n):
            valsRowCount[tuple(grid[row])] += 1
        
        for col in range(n):
            vals = tuple([grid[i][col] for i in range(n)])
            equals += valsRowCount[vals]

        return equals

# Unit Tests
import unittest
funcs = [Solution().equalPairs]

class TestEqualPairs(unittest.TestCase):
    def testEqualPairs1(self):
        for equalPairs in funcs:
            grid = [[3,2,1],[1,7,6],[2,7,7]]
            self.assertEqual(equalPairs(grid=grid), 1)

    def testEqualPairs2(self):
        for equalPairs in funcs:
            grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
            self.assertEqual(equalPairs(grid=grid), 3)

if __name__ == "__main__":
    unittest.main()