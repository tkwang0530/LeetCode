"""
934. Shortest Bridge
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Example1:
Input: grid = [[0,1],[1,0]]
Output: 1

Example2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:
n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""

"""
Note:
1. DFS + BFS: O(mn) time | O(mn) space - where m is len(grid) and n is len(grid[0])
"""

from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        currentPointSet = set()
        def dfs(row, col, label):
            for nextRow, nextCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if nextRow in (-1, rows) or nextCol in (-1, cols) or grid[nextRow][nextCol] != 1:
                    continue

                grid[nextRow][nextCol] = label
                currentPointSet.add((nextRow, nextCol))
                dfs(nextRow, nextCol, label)

        label = 2
        found = False
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    grid[row][col] = label
                    currentPointSet.add((row, col))
                    dfs(row, col, label)
                    found = True
                    break
            if found:
                break
        
        steps = 0
        while currentPointSet:
            nextPointSet = set()
            for row, col in currentPointSet:
                for nextRow, nextCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if nextRow in (-1, rows) or nextCol in (-1, cols) or grid[nextRow][nextCol] == label:
                        continue
                    if grid[nextRow][nextCol] == 1:
                        return steps

                    # grid[nextRow][nextCol] = 0
                    nextPointSet.add((nextRow, nextCol))
                    grid[nextRow][nextCol] = label
            
            currentPointSet = nextPointSet
            steps += 1
        return steps

# Unit Tests
import unittest
funcs = [Solution().shortestBridge]


class TestShortestBridge(unittest.TestCase):
    def testShortestBridge1(self):
        for shortestBridge in funcs:
            grid = [[0,1],[1,0]]
            self.assertEqual(shortestBridge(grid=grid), 1)

    def testShortestBridge2(self):
        for shortestBridge in funcs:
            grid = [[0,1,0],[0,0,0],[0,0,1]]
            self.assertEqual(shortestBridge(grid=grid), 2)

    def testShortestBridge3(self):
        for shortestBridge in funcs:
            grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
            self.assertEqual(shortestBridge(grid=grid), 1)

if __name__ == "__main__":
    unittest.main()
