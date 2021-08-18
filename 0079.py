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
1. Recursive Backtracking (DFS with set): O(n * m * 4^L) time | O(L) space
2. Recursive Backtracking (DFS without set): O(n * m * 4^L) time | O(L) space
"""

from typing import List
import unittest
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()
        for row in range(rows):
            for col in range(cols):
                if self.dfs(board, row, col, word, 0, path):
                    return True
        return False

    def dfs(self, board, row, col, word, index, path):
        if index == len(word):
            return True
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or word[index] != board[row][col] or (row, col) in path:
            return False
        path.add((row, col))
        result = (self.dfs(board, row + 1, col, word, index + 1, path) or
                        self.dfs(board, row - 1, col, word, index + 1, path) or
                        self.dfs(board, row, col + 1, word, index + 1, path) or
                        self.dfs(board, row, col - 1, word, index + 1, path))
        path.remove((row, col))
        return result

    def exist2(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if self.dfs2(board, row, col, word, 0):
                    return True
        return False
        
    def dfs2(self, board, row, col, word, index) -> bool:
        if index == len(word):
            return True
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or board[row][col] != word[index]:
            return False
        temp, board[row][col] = board[row][col], "#"
        result = (self.dfs2(board, row - 1, col, word, index + 1) or
                 self.dfs2(board, row + 1, col, word, index + 1) or
                 self.dfs2(board, row, col - 1, word, index + 1) or
                 self.dfs2(board, row, col + 1, word, index + 1))
        board[row][col] = temp
        return result


# Unit Tests
funcs = [Solution().exist, Solution().exist2]


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
