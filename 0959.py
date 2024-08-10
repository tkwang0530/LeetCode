"""
959. Regions Cut By Slashes
description: https://leetcode.com/problems/regions-cut-by-slashes/description/
"""

""" 
1. dfs + HashTable: O(mn) time | O(mn) space - where m is len(grid) and n is len(grid[0])
ref: https://www.youtube.com/watch?v=j8KrBYIxHK8
"""
from typing import List
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows1, cols1 = len(grid), len(grid[0])
        rows2, cols2 = 3 * rows1, 3 * cols1
        grid2 = [[0] * cols2 for _ in range(rows2)]

        for r in range(rows1):
            for c in range(cols1):
                r2, c2 = r * 3, c * 3
                if grid[r][c] == "/":
                    grid2[r2][c2+2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2] = 1
                elif grid[r][c] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2+2] = 1

        visited = set()
        def dfs(r, c):
            if  (r, c) in visited:
                return
            if grid2[r][c] == 1:
                return

            visited.add((r, c))
            for nextR, nextC in [(r+1,c), (r, c+1), (r-1, c), (r, c-1)]:
                if nextR in (-1, rows2) or nextC in (-1, cols2):
                    continue
                dfs(nextR, nextC)

        regions = 0
        for r in range(rows2):
            for c in range(cols2):
                if grid2[r][c] == 0 and (r, c) not in visited:
                    dfs(r, c)
                    regions += 1

        return regions

# Unit Tests
import unittest
funcs = [Solution().regionsBySlashes]


class TestPeakIndexInMountainArray(unittest.TestCase):
    def testPeakIndexInMountainArray1(self):
        for regionsBySlashes in funcs:
            grid = [" /","/ "]
            self.assertEqual(regionsBySlashes(grid=grid), 2)

    def testPeakIndexInMountainArray2(self):
        for func in funcs:
            grid = [" /","  "]
            self.assertEqual(func(grid=grid), 1)

    def testPeakIndexInMountainArray3(self):
        for func in funcs:
            grid = ["/\\","\\/"]
            self.assertEqual(func(grid=grid), 5)

if __name__ == "__main__":
    unittest.main()
