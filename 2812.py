"""
2812. Find the Safest Path in a Grid
You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

Example1:
Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 0
Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

Example2:
Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

Example3:
Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

Constraints:
1 <= grid.length == n <= 400
grid[i].length == n
grid[i][j] is either 0 or 1.
There is at least one thief in the grid.
"""

"""
Note:
1. BFS + Dijkstra: O(n^2*log(n)) time | O(n^2) space - where n is the length of array grid
2. BFS (layer order traversal) + Dijkstra (max heap): O(n^2*log(n)) time | O(n^2) space - where n is the length of array grid
"""

import collections
import heapq
from typing import List
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        copyGrid = [[0] * cols for _ in range(rows)]
        queue = collections.deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    copyGrid[row][col] = 1

        while queue:
            row, col = queue.popleft()
            for nextRow, nextCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if nextRow in (-1, rows) or nextCol in (-1, cols):
                    continue
                
                if copyGrid[nextRow][nextCol] > 0:
                    continue
                
                copyGrid[nextRow][nextCol] = copyGrid[row][col]+1
                queue.append((nextRow, nextCol))
        
        maxHeap = [(-copyGrid[0][0],0,0)]
        safeness = rows+cols

        visited = set()
        while maxHeap:
            negativeVal, row, col = heapq.heappop(maxHeap)
            val = -1*negativeVal
            safeness = min(safeness, val-1)
            if row == rows-1 and col == cols-1:
                return safeness
            for nextRow, nextCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if nextRow in (-1, rows) or nextCol in (-1, cols):
                    continue
                
                if (nextRow, nextCol) in visited:
                    continue

                val = copyGrid[nextRow][nextCol]
                heapq.heappush(maxHeap, (-val, nextRow, nextCol))
                visited.add((nextRow, nextCol))
        return safeness

class Solution2:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        currentNodes = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    currentNodes.append((row, col))

        # BFT (layer order traversal)
        number = 2
        while currentNodes:
            nextNodes = []
            for r, c in currentNodes:
                for nextRow, nextCol in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if nextRow in (-1, rows) or nextCol in (-1, cols):
                        continue

                    if grid[nextRow][nextCol] > 0:
                        continue

                    grid[nextRow][nextCol] = number
                    nextNodes.append((nextRow, nextCol))
            currentNodes = nextNodes
            number += 1
        
        # dijkstra algorithm
        maxHeap = [(-grid[0][0], 0, 0)] # (-number, row, col)
        locMinNumber = collections.defaultdict(lambda: float("-inf"))
        locMinNumber[(0,0)] = grid[0][0]
        while maxHeap:
            negNumber, row, col = heapq.heappop(maxHeap)
            number = -negNumber

            if number < locMinNumber[(row, col)]:
                continue

            locMinNumber[(row, col)] = number
            if row == rows-1 and col == cols-1:
                return number-1

            for nextRow, nextCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if nextRow in (-1, rows) or nextCol in (-1, cols):
                    continue

                newMinNumber = min(number, grid[nextRow][nextCol])
                if newMinNumber <= locMinNumber[(nextRow, nextCol)]:
                    continue

                locMinNumber[(nextRow, nextCol)] = newMinNumber
                heapq.heappush(maxHeap, (-newMinNumber, nextRow, nextCol))
        return -1

# Unit Tests
import unittest
funcs = [Solution().maximumSafenessFactor, Solution2().maximumSafenessFactor]


class TestMaximumSafenessFactor(unittest.TestCase):
    def testMaximumSafenessFactor1(self):
        for func in funcs:
            grid = [[1,0,0],[0,0,0],[0,0,1]]
            self.assertEqual(func(grid=grid), 0)

    def testMaximumSafenessFactor2(self):
        for func in funcs:
            grid = [[0,0,1],[0,0,0],[0,0,0]]
            self.assertEqual(func(grid=grid), 2)

if __name__ == "__main__":
    unittest.main()
