"""
64. Mininum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example1:
Input: grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1],
]
Output: 7
Explanation: Because the path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum.

Example2:
Input: grid = [
    [1, 2, 3],
    [4, 5, 6]
]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
= <= grid[i][j] <= 100
"""

"""
1. Recursion: O(2^(m+n)) time | O(m+n) space
2. Recursion + caching: O(mn) time | O(mn) space
3. DP: O(mn) time | O(mn) space
4. DP (improved): O(mn) time | O(n) space
"""




from typing import List
import unittest
class Solution(object):
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.minPathSumHelper(grid, len(grid) - 1, len(grid[0]) - 1)

    def minPathSumHelper(self, grid, i, j) -> int:
        if i == 0 and j == 0:
            return grid[i][j]
        if i == 0:
            return grid[i][j] + self.minPathSumHelper(grid, i, j - 1)
        if j == 0:
            return grid[i][j] + self.minPathSumHelper(grid, i-1, j)
        return grid[i][j] + min(self.minPathSumHelper(grid, i, j-1), self.minPathSumHelper(grid, i-1, j))

    def minPathSum2(self, grid: List[List[int]]) -> int:
        memo = {(0,0): grid[0][0]}
        return self.minPathSumHelper2(grid, len(grid)-1, len(grid[0])-1, memo)
    
    def minPathSumHelper2(self, grid, row, col, memo) -> int:
        if (row, col) in memo:
            return memo[(row, col)]
        
        if row == 0:
            memo[(row, col)] = grid[row][col] + self.minPathSumHelper2(grid, row, col-1, memo)
        elif col == 0:
            memo[(row, col)] = grid[row][col] + self.minPathSumHelper2(grid, row - 1, col, memo)
        else:
            memo[(row, col)] = grid[row][col] + min(self.minPathSumHelper2(grid, row, col - 1, memo), self.minPathSumHelper2(grid, row - 1, col, memo))
        
        return memo[(row, col)]

    def minPathSum3(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cost = []
        for _ in range(rows):
            cost.append([0] * cols)
        cost[0][0] = grid[0][0]
        for row in range(1, rows):  # first col
            cost[row][0] = grid[row][0] + cost[row-1][0]
        for col in range(1, cols):  # first row
            cost[0][col] = grid[0][col] + cost[0][col-1]
        for row in range(1, rows):
            for col in range(1, cols):
                cost[row][col] = grid[row][col] + min(cost[row-1][col], cost[row][col-1])
        return cost[-1][-1]

    def minPathSum4(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cost = [0] * cols

        cost[0] = grid[0][0]
        for col in range(1, cols):
            cost[col] = cost[col-1] + grid[0][col]

        for row in range(1, rows):
            cost[0] += grid[row][0]
            for col in range(1, cols):
                cost[col] = grid[row][col] + min(cost[col-1], cost[col])
        return cost[-1]


# Unit Tests
funcs = [Solution().minPathSum, Solution().minPathSum2,
         Solution().minPathSum3, Solution().minPathSum4]


class TestMinPathSum(unittest.TestCase):
    def testMinPathSum1(self):
        for func in funcs:
            grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
            self.assertEqual(func(grid=grid), 7)

    def testMinPathSum2(self):
        for func in funcs:
            grid = [[1, 2, 3], [4, 5, 6]]
            self.assertEqual(func(grid=grid), 12)


if __name__ == "__main__":
    unittest.main()
