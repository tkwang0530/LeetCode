"""
1293. Shortest Path in a Grid with Obstacles Elimination
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move, up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

Example1:
Input: 
grid = [
    [0,0,0],
    [1,1,0],
    [0,0,0],
    [0,1,1],
    [0,0,0]
], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example2:
Input: grid = [
    [0,1,1],
    [1,1,1],
    [1,0,0]
], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.

Constraints:
m == grid.length
n == grid[i].length
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
"""

"""
1. Iterative BFS with Matrix: O(m*n*k) time | O(m*n*k) space
(1) Do we need a visited set to mark whether we visited this cell before?
No. Because we can visit the same cell many times. as the obstacles in this path are fewer => save the minimum obstacles we saw in this path

(2) Breadth-first search
Find a shortest path in an unweighted undirected graph.

(3) When to exit?
Once we reach the end, return the length

(4) Time Complexity and Space Complexity
Because for every cell[m][n], in the worst case we have to put that cell into the queue/bfs k times
"""

from typing import List
from collections import deque
import unittest
class Solution(object):
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        seen = []
        for _ in range(m):
            seen.append([float("inf")] * n)
        seen[0][0] = 0
        queue = deque([(0, 0, 0)]) # (row, col, numOfObstacles)
        steps = 0
        while queue:
            size = len(queue)
            for i in range(size):
                row, col, numOfObStacles = queue.popleft()
                if row == m - 1 and col == n - 1:
                    return steps
                directions = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
                for r, c in directions:
                    if r in (-1, m) or c in (-1, n):
                        continue
                    newNumOfObstacles = numOfObStacles + grid[r][c]
                    if newNumOfObstacles >= seen[r][c] or newNumOfObstacles > k:
                        continue
                    seen[r][c] = newNumOfObstacles
                    queue.append((r, c, newNumOfObstacles))
            steps += 1
        return -1

# Unit Tests
funcs = [Solution().shortestPath]


class TestShortestPath(unittest.TestCase):
    def testShortestPath1(self):
        for func in funcs:
            grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]] 
            k = 1
            self.assertEqual(func(grid=grid, k=k), 6)

    def testShortestPath2(self):
        for func in funcs:
            grid = [[0,1,1],[1,1,1],[1,0,0]]
            k = 1
            self.assertEqual(func(grid=grid, k=k), -1)

if __name__ == "__main__":
    unittest.main()
