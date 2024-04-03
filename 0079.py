"""
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example1:
Input: board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
], word = "ABCCED"
Output: true


Example2:
Input: board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
], word = "SEE"
Output: true

Example3:
Input: board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""

"""
Note:
1. backtracking: O(n * m * 4^L) time | O(L) space - where n is the number of rows in the board, m is the number of columns in the board, and L is the length of the word
"""

from typing import List
import unittest
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row: int, col: int, i: int) -> bool:
            if i == len(word):
                return True

            char = board[row][col]
            if char != word[i]:
                return False

            if i == len(word) - 1:
                return True
            
            canAchieve = False
            for nextRow, nextCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if nextRow in (-1, rows) or nextCol in (-1, cols):
                    continue

                if (nextRow, nextCol) in visited:
                    continue

                visited.add((nextRow, nextCol))
                canAchieve = canAchieve or dfs(nextRow, nextCol, i+1)
                visited.remove((nextRow, nextCol))
            
            return canAchieve

        visited = set()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    visited.add((row, col))
                    if dfs(row, col, 0):
                        return True
                    visited.remove((row, col))
        return False

# Unit Tests
funcs = [Solution().exist]


class TestExist(unittest.TestCase):
    def testExist1(self):
        for func in funcs:
            board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
            word = "ABCCED"
            self.assertEqual(func(board=board, word=word), True)

    def testExist2(self):
        for func in funcs:
            board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
            word = "SEE"
            self.assertEqual(func(board=board, word=word), True)

    def testExist3(self):
        for func in funcs:
            board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
            word = "ABCB"
            self.assertEqual(func(board=board, word=word), False)

if __name__ == "__main__":
    unittest.main()
