"""
2392. Build a Matrix With Conditions
description: https://leetcode.com/problems/build-a-matrix-with-conditions/description/
"""

"""
Note:
1. Topological Sort + HashMap: O(k^2) time | O(k^2) space
ref: https://www.youtube.com/watch?v=khTKB1PzCuw
"""

from typing import List
import collections
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, graph, visited, path, order):
            if src in path:
                return False
            if src in visited:
                return True

            visited.add(src)
            path.add(src)
            for neighbor in graph[src]:
                if not dfs(neighbor, graph, visited, path, order):
                    return False

            path.remove(src)
            order.append(src)
            return True

        def toposort(edges):
            graph = collections.defaultdict(list)
            for u, v in edges:
                graph[u].append(v)

            visited, path = set(), set()
            order = []
            for src in range(1, k+1):
                if not dfs(src, graph, visited, path, order):
                    return []

            return order[::-1]
        
        rowOrder = toposort(rowConditions)
        colOrder = toposort(colConditions)

        if not rowOrder or not colOrder:
            return []

        valToRow = {num: i for i, num in enumerate(rowOrder)}
        valToCol = {num: i for i, num in enumerate(colOrder)}
        grid = [[0] * k for _ in range(k)]
        for num in range(1, k+1):
            row, col = valToRow[num], valToCol[num]
            grid[row][col] = num

        return grid

# Unit Tests
import unittest
funcs = [Solution().buildMatrix]
def checker(grid, rowConditions, colConditions):
    rows  = len(grid)
    cols = len(grid)
    numPositionMap = {}
    for row in range(rows):
        for col in range(cols):
            num = grid[row][col]
            if num == 0:
                continue
            if num in numPositionMap:
                return False
            numPositionMap[num] = (row, col)

    for cond in rowConditions:
        above, below = cond
        if numPositionMap[above][0] >= numPositionMap[below][0]:
            return False
        
    for cond in colConditions:
        left, right = cond
        if numPositionMap[left][1] >= numPositionMap[right][1]:
            return False

    return True

class TestMinIncrementForUnique(unittest.TestCase):
    def testMinIncrementForUnique1(self):
        for func in funcs:
            k = 3
            rowConditions = [[1,2],[3,2]]
            colConditions = [[2,1],[3,2]]
            grid = func(k, rowConditions, colConditions)
            self.assertTrue(checker(grid, rowConditions, colConditions))


    def testMinIncrementForUnique2(self):
        for func in funcs:
            k = 3
            rowConditions = [[1,2],[2,3],[3,1],[2,3]]
            colConditions = [[2,1]]
            grid = func(k, rowConditions, colConditions)
            self.assertEqual(grid, [])


if __name__ == "__main__":
    unittest.main()
