"""
212. Word Search II
Given an m x n grid of characters board and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example1:
Input: board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]


Example2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters
All the strings of words are unique.
"""

"""
Note:
1. Recursive Backtracking (DFS with Trie): O(k*l + m*n*4^l) time | O(k*l + l) space
where l is the average length of the each word
where k is length of words
"""

from typing import List
import unittest

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        result = []
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                chars = []
                self.dfs(board, row, col, root, chars, result)
        return result
    
    def dfs(self, board, row, col, node, chars, result) -> None:
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or board[row][col] not in node.children:
            return
        char = board[row][col]
        chars.append(char)
        node = node.children[char]
        if node.isWord:
            result.append("".join(chars))
            node.isWord = False
        board[row][col] = "#"
        directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for r, c in directions:
            self.dfs(board, r, c, node, chars, result)
        chars.pop()
        board[row][col] = char


# Unit Tests
funcs = [Solution().findWords]


class TestFindWords(unittest.TestCase):
    def testFindWords1(self):
        for func in funcs:
            board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
            words = ["oath","pea","eat","rain"]
            self.assertEqual(sorted(func(board=board, words=words)), sorted(["eat","oath"]))

    def testFindWords2(self):
        for func in funcs:
            board = [["a","b"],["c","d"]]
            words = ["abcb"]
            self.assertEqual(sorted(func(board=board, words=words)), sorted([]))

if __name__ == "__main__":
    unittest.main()
