"""
2658. Maximum Number of Fish in a Grid
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Example1:
Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

Example2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 

Constraints:
m == grid.length
m == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
"""

"""
Note:
1. UnionFind: O(mn) time | O(mn) space - where m is the length of row, n is the length of col
"""




import unittest
from typing import List
class UnionFind:
    def __init__(self, grid):
        rows, cols = len(grid), len(grid[0])
        total = rows * cols
        self.parents = [i for i in range(total)]
        self.ranks = [1 for _ in range(total)]
        self.counts = [grid[i//cols][i % cols] for i in range(total)]

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return max(self.counts[pu], self.counts[pv])

        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
            self.counts[pv] += self.counts[pu]
        elif self.ranks[pv] < self.ranks[pu]:
            self.parents[pv] = pu
            self.counts[pu] += self.counts[pv]
        else:
            self.parents[pv] = pu
            self.counts[pu] += self.counts[pv]
            self.ranks[pu] += 1

        newCount = max(self.counts[pu], self.counts[pv])
        return newCount


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        maxFish = 0
        unionFind = UnionFind(grid)
        rows, cols = len(grid), len(grid[0])

        def convert(r, c):
            return r*cols + c

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0:
                    u = convert(row, col)
                    maxFish = max(maxFish, grid[row][col])
                    if row+1 < rows and grid[row+1][col] > 0:
                        vD = convert(row+1, col)
                        maxFish = max(maxFish, unionFind.union(u, vD))
                    if col+1 < cols and grid[row][col+1] > 0:
                        vR = convert(row, col+1)
                        maxFish = max(maxFish, unionFind.union(u, vR))
        return maxFish


# Unit Tests
funcs = [Solution().findMaxFish]


class TestFindMaxFish(unittest.TestCase):
    def testFindMaxFish1(self):
        for func in funcs:
            grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
            self.assertEqual(func(grid=grid), 7)

    def testFindMaxFish2(self):
        for func in funcs:
            grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
            self.assertEqual(func(grid=grid), 1)


if __name__ == "__main__":
    unittest.main()
