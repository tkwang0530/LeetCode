"""
1631. Path With Minimum Effort
description: https://leetcode.com/problems/path-with-minimum-effort/description/
"""

"""
Note:
1. Dijkstra: O(ElogE) time | O(E) space - where E = 2mn
"""

from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = set()
        minHeap = [(0, 0, 0)] # (effort, row, col)
        minEffort = 0
        rows = len(heights)
        cols = len(heights[0])
        while minHeap:
            effort, row, col = heapq.heappop(minHeap)
            if (row,col) in visited:
                continue
            visited.add((row,col))
            minEffort = max(minEffort, effort)
            if row == rows - 1 and col == cols - 1:
                break
            for nextRow, nextCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if (nextRow,nextCol) in visited:
                    continue
                if nextRow in (-1, rows) or nextCol in (-1, cols):
                    continue
                nextEffort = abs(heights[nextRow][nextCol] - heights[row][col])
                heapq.heappush(minHeap, (nextEffort, nextRow, nextCol))
        return minEffort                

# Unit Tests
import unittest
funcs = [Solution().minimumEffortPath]
class TestMinimumEffortPath(unittest.TestCase):
    def testMinimumEffortPath1(self):
        for minimumEffortPath in funcs:
            heights = [[1,2,2],[3,8,2],[5,3,5]]
            self.assertEqual(minimumEffortPath(heights=heights), 2)

    def testMinimumEffortPath2(self):
        for minimumEffortPath in funcs:
            heights = [[1,2,3],[3,8,4],[5,3,5]]
            self.assertEqual(minimumEffortPath(heights=heights), 1)

    def testMinimumEffortPath3(self):
        for minimumEffortPath in funcs:
            heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
            self.assertEqual(minimumEffortPath(heights=heights), 0)

if __name__ == "__main__":
    unittest.main()
