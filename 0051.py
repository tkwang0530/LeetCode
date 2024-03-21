"""
51. N-Queens
description: https://leetcode.com/problems/n-queens/description/
"""

"""
Note:
1. Backtracking: O(n!) time | O(n^2) space
"""

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiags = set() # r+c
        negDiags = set() # r-c
        output = []
        board = [["."] * n for _ in range(n)]
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                output.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r-c) in negDiags or (r+c) in posDiags:
                    continue

                cols.add(c)
                negDiags.add(r-c)
                posDiags.add(r+c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                negDiags.remove(r-c)
                posDiags.remove(r+c)
                board[r][c] = "."

        backtrack(0)
        return output

# Unit Tests
import unittest
funcs = [Solution().solveNQueens]

class TestSolveNQueens(unittest.TestCase):
    def testSolveNQueens1(self):
        for func in funcs:
            n = 4
            self.assertEqual(func(n=n), [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])

    def testSolveNQueens2(self):
        for func in funcs:
            n = 1
            self.assertEqual(func(n=n), [["Q"]])

if __name__ == "__main__":
    unittest.main()