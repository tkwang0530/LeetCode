"""
688. Knight Probability in Chessboard
On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.

Example1:
Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

Example2:
Input: n = 1, k = 0, row = 0, column = 0
Output: 1.00000

Constraints:
1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n
"""

"""
Note:
1. Conditional Probability + DFS + HashMap: O(n^2 * k) time | O(n^2 * k) space
"""

from typing import List, Tuple
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def isInBoard(row, col) -> bool:
            return 0 <= row and row <= n-1 and 0 <= col and col <= n-1

        def getNextMoves(row, col) -> List[Tuple[int, int]]:
            return [
                (row-1, col+2), 
                (row-2, col+1), 
                (row+1, col+2), 
                (row+2, col+1), 
                (row+2, col-1), 
                (row+1, col-2), 
                (row-1, col-2), 
                (row-2, col-1)
            ]

        cache = {}
        def getValidNextMoves(row, col) -> List[Tuple[int, int]]:
            if (row, col) in cache:
                return cache[(row, col)]
            nextMoves = getNextMoves(row, col)
            cache[(row, col)] = [(r, c) for r, c in nextMoves if isInBoard(r, c)]
            return cache[(row, col)]
        
        memo = {}
        def dfs(row, col, weight, moves) -> float:
            if moves == k:
                return weight * isInBoard(row, col)

            if (row, col, moves) in memo:
                return memo[(row, col, moves)]

            prob = 0
            validNextMoves = getValidNextMoves(row, col)
            for validNextMove in validNextMoves:
                nextRow, nextCol = validNextMove
                memo[(nextRow, nextCol, moves)] = dfs(nextRow, nextCol, weight/8, moves+1)
                prob += memo[(nextRow, nextCol, moves)]
            memo[(row, col, moves)] = prob
            return memo[(row, col, moves)]
        return dfs(row, column, 1, 0)

            

# Unit Tests
import unittest
funcs = [Solution().knightProbability]

class TestKnightProbability(unittest.TestCase):
    def testKnightProbability1(self):
        for func in funcs:
            n = 3
            k = 2
            row = 0
            column = 0
            self.assertEqual(func(n=n, k=k, row=row, column=column), 0.06250)

    def testKnightProbability2(self):
        for func in funcs:
            n = 1
            k = 0
            row = 0
            column = 0
            self.assertEqual(func(n=n, k=k, row=row, column=column), 1.0000)

if __name__ == "__main__":
    unittest.main()
