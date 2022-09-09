"""
52. N-Queens II
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 9
"""

"""
Note:
1. DFS (Bottom-up): O(n^n) time | O(3n) space
"""




import unittest
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag = set()
        antiDiag = set()

        def dfs(x: int) -> int:
            if x >= n:
                return 1
            ans = 0
            for y in range(n):
                if y in cols or x-y in diag or x+y in antiDiag:
                    continue
                cols.add(y)
                diag.add(x-y)
                antiDiag.add(x+y)

                ans += dfs(x + 1)

                cols.remove(y)
                diag.remove(x-y)
                antiDiag.remove(x+y)
            return ans
        return dfs(0)


# Unit Tests
funcs = [Solution().totalNQueens]


class TestTotalNQueens(unittest.TestCase):
    def testTotalNQueens1(self):
        for func in funcs:
            n = 4
            self.assertEqual(func(n=n), 2)

    def testTotalNQueens2(self):
        for func in funcs:
            n = 1
            self.assertEqual(func(n=n), 1)


if __name__ == "__main__":
    unittest.main()
