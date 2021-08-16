"""
130. Surrounded Regions
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example1:
Input: board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]
Output: [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]
]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example2:
Input: board = [["X"]]
Output: [["X"]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'
"""

"""
Note:
1. Recursive DFS from the sides: O(mn) time | O(mn) space
capture surrounded regions = capture everything except unsurrounded regions
"""

from typing import List
import unittest
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        # Capture unsurrounded regions
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row in [0, rows - 1] or col in [0, cols - 1]):
                    self.dfs(board, row, col)

        # Capture surrounded regions (O -> X, T -> O )
        for row in range(rows):
            for col in range(cols):
                board[row][col] = 'O' if board[row][col] == 'T' else 'X'

    def dfs(self, board, row, col):
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or board[row][col] != "O":
            return
        board[row][col] = "T"
        self.dfs(board, row + 1, col)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col - 1)
        self.dfs(board, row, col + 1)


# Unit Tests
funcs = [Solution().solve]


class TestSolve(unittest.TestCase):
    def testSolve1(self):
        for func in funcs:
            board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
            func(board=board)
            self.assertEqual(board, [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])

    def testSolve2(self):
        for func in funcs:
            board = [["X"]]
            func(board=board)
            self.assertEqual(board, [["X"]])


if __name__ == "__main__":
    unittest.main()
