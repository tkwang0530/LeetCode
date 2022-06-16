"""
305. Number of Islands II
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [r_i, c_i] is the position (r_i, c_i) at which we should operate the i-th operations.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (r_i, c_i) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example1:
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.

Example2:
Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]

Constraints:
1 <= m, n, positions.length <= 10^4
1 <= m * n <= 10^4
positions[i].length == 2
0 <= r_i < m
0 <= c_i < n
"""

"""
Note:
1. UnionFind + HashTable: O(nm+p) time | O(nm+p) space - where m is the length of row, n is the length of col, and p is the length of positions
"""
from typing import List
class UnionFind:
    def __init__(self, total):
        self.parents = [i for i in range(total)]
        self.ranks = [1 for _ in range(total)]
        self.parentsCount = 0
        
    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
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
        self.parentsCount -= 1
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        output = []
        unionFind = UnionFind(m*n)
        def findIndex(row, col):
            return row*n + col
        
        landsSet = set()
        for row, col in positions:
            if (row, col) not in landsSet:
                unionFind.parentsCount += 1
            landsSet.add((row, col))
            for diffRow, diffCol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nextRow, nextCol = row+diffRow, col+diffCol
                if nextRow in (-1,m) or nextCol in (-1,n):
                    continue
                
                if (nextRow, nextCol) not in landsSet:
                    continue
                
                unionFind.union(findIndex(row, col), findIndex(nextRow, nextCol))
            output.append(unionFind.parentsCount)
                
        return output

# Unit Tests
import unittest
funcs = [Solution().numIslands2]
class TestNumIslands2(unittest.TestCase):
    def testNumIslands2_1(self):
        for func in funcs:
            m = 3
            n = 3
            positions = [[0,0],[0,1],[1,2],[2,1]]
            self.assertEqual(func(m=m, n=n, positions=positions), [1,1,2,3])

    def testNumIslands2_2(self):
        for func in funcs:
            m = 1
            n = 1
            positions = [[0,0]]
            self.assertEqual(func(m=m, n=n, positions=positions), [1])

if __name__ == "__main__":
    unittest.main()
