"""
37. Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.' .
It is guaranteed that the input board has only one solution.
"""

"""
Note:
1. HashTable + Backtracking
"""

from typing import List
import unittest, collections
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        blockNums = collections.defaultdict(set)
        rowNums = collections.defaultdict(set)
        colNums = collections.defaultdict(set)

        for row in range(rows):
            for col in range(cols):
                val = board[row][col]
                if val == ".":
                    continue
                if val in blockNums[(row//3, col//3)]:
                    return
                if val in rowNums[row] or val in colNums[col]:
                    return
                blockNums[(row//3, col//3)].add(val)
                rowNums[row].add(val)
                colNums[col].add(val)
        
        def dfs(row, col, container) -> bool:
            if row == rows or container[0]:
                return True
            if col == cols:
                return dfs(row+1, 0, container)
            if board[row][col] != ".":
                return dfs(row, col+1, container)
            
            solvable = False
            for num in range(1, 9+1):
                numStr = str(num)
                if numStr in blockNums[(row//3, col//3)]:
                    continue
                
                if numStr in rowNums[row] or numStr in colNums[col]:
                    continue

                board[row][col] = numStr
                blockNums[(row//3, col//3)].add(numStr)
                rowNums[row].add(numStr)
                colNums[col].add(numStr)
                solvable = solvable or dfs(row, col+1, container)
                if solvable:
                    container[0] = True
                    return True
                # backtrack
                board[row][col] = "."
                blockNums[(row//3, col//3)].remove(numStr)
                rowNums[row].remove(numStr)
                colNums[col].remove(numStr)
            return solvable
        container = [False]
        dfs(0, 0, container)

# Unit Tests
funcs = [Solution().solveSudoku]


class TestSolveSudoku(unittest.TestCase):
    def testSolveSudoku1(self):
        for func in funcs:
            board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
            solution = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
            func(board=board)
            self.assertEqual(board, solution)

if __name__ == "__main__":
    unittest.main()
