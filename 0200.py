"""
200. Number of Islands
description: https://leetcode.com/problems/number-of-islands/description/
"""

"""
Note:
1. Recursion (DFS): O(nm) time | O(nm) space
2. Iteration (BFS): O(nm) time | O(nm) space
3. UnionFind: O(nm) time | O(nm) space
"""




from collections import deque
from typing import List
import unittest
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge
        if not grid:
            return 0
        
        def isWater(row, col):
            return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0"
        
        def dfs(row, col):
            if isWater(row, col):
                return
            grid[row][col] = "0"
            directions = [(row - 1, col), (row + 1, col),
                        (row, col + 1), (row, col - 1)]
            for x, y in directions:
                dfs(x, y)

        numOfIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    numOfIslands += 1
        return numOfIslands

    

class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def isWater(row, col):
            return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0"
        
        def bfs(row, col):
            queue = deque([(row, col)])
            while queue:
                currentRow, currentCol = queue.popleft()
                directions = [(currentRow + 1, currentCol), (currentRow - 1, currentCol),
                            (currentRow, currentCol + 1), (currentRow, currentCol - 1)]
                for x, y in directions:
                    if not isWater(x, y):
                        queue.append((x, y))
                        grid[x][y] = "0"

        numOfIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    bfs(row, col)
                    numOfIslands += 1
        return numOfIslands

class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

    def find(self, u: int) -> int:
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False

        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pv] < self.ranks[pu]:
            self.parents[pv] = pu
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1
        return True

class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        uf = UnionFind(rows*cols)
    
        def getIdx(row: int, col: int) -> int:
            return row * cols + col
        
        islandSet = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0":
                    continue

                u = getIdx(row, col)
                if row < rows-1 and grid[row+1][col] == "1":
                    uf.union(u, getIdx(row+1, col))

                if col < cols-1 and grid[row][col+1] == "1":
                    uf.union(u, getIdx(row, col+1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0":
                    continue

                u = getIdx(row, col)
                islandSet.add(uf.find(u))
        return len(islandSet)


# Unit Tests
funcs = [Solution().numIslands, Solution2().numIslands, Solution3().numIslands]


class TestNumIslands(unittest.TestCase):
    def testNumIslands1(self):
        for func in funcs:
            grid = [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ]
            self.assertEqual(func(grid=grid), 3)

    def testNumIslands2(self):
        for func in funcs:
            grid = [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ]
            self.assertEqual(func(grid=grid), 1)


if __name__ == "__main__":
    unittest.main()
