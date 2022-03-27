"""
1510. Stone Game IV
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

Example1:
Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.

Example2:
Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

Example3:
Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

Constraints:
1 <= n <= 10^5
"""

""" 
1. dfs+memo: O(n*sqrt(n)) time | O(n) space
2. dp: O(n*sqrt(n)) time | O(n) space
"""

import math
class Solution(object):
    def winnerSquareGame(self, n: int) -> bool:
        # dfs(n) return if player can win with given n stones
        memo = {}
        def dfs(n) -> bool:
            if n in memo:
                return memo[n]
            
            canWin = False
            for i in range(int(math.sqrt(n)), 0, -1):
                if n-i*i == 0:
                    canWin = True
                    break
                canWin = canWin or (not dfs(n-i*i))
            memo[n] = canWin
            return memo[n]
        return dfs(n)

    def winnerSquareGame2(self, n: int) -> bool:
        # dp[n] return if player can win with given n stones
        # 0: unknown, 1: canWin, 2: cannotWin
        dp = [0] * (n+1)
        for i in range(n+1):
            if dp[i] != 0:
                continue
            
            if i == 0:
                dp[i] = 2
                continue
            if i == 1:
                dp[i] = 1
                continue

            canWin = False
            for j in range(int(math.sqrt(i)), 0, -1):
                canWin = canWin or (dp[i-j**2] == 2)
            dp[i] = 1 if canWin else 2
        return dp[n] == 1

# Unit Tests
import unittest
funcs = [Solution().winnerSquareGame, Solution().winnerSquareGame2]

class TestWinnerSquareGame(unittest.TestCase):
    def testWinnerSquareGame1(self):
        for func in funcs:
            n = 1
            self.assertEqual(func(n=n), True)

    def testWinnerSquareGame2(self):
        for func in funcs:
            n = 2
            self.assertEqual(func(n=n), False)

    def testWinnerSquareGame3(self):
        for func in funcs:
            n = 4
            self.assertEqual(func(n=n), True)

    def testWinnerSquareGame4(self):
        for func in funcs:
            n = 8
            self.assertEqual(func(n=n), True)

if __name__ == "__main__":
    unittest.main()
