"""
877. Stone Game
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with "Alice starting first". Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

Example1:
Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

Example2:
Input: piles = [3,7,2,3]
Output: true

Constraints:
2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles[i]) is odd.
"""

"""
Note:
1. dfs with cache: O(n^2) time | O(n^2) space
2. smart choose all odd or all even piles: O(1) time | O(1) space
3. DP: O(n^2) time | O(n^2) space
4. DP(improved): O(n^2) time | O(n) space
"""

import unittest
from typing import List, Dict
class Solution(object):
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {} # subarr piles (left, right) -> Max Alice Total

        # return max alice total
        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            
            # check if this round is Alice or Bob
            isAliceTurn = (right - left + 1) % 2 == 0
            leftPile = piles[left] if isAliceTurn else 0
            rightPile = piles[right] if isAliceTurn else 0

            if isAliceTurn:
                cache[(left, right)] = max(dfs(left + 1, right) + leftPile,
                        dfs(left, right - 1) + rightPile)
            else:
                cache[(left, right)] = min(dfs(left + 1, right) + leftPile,
                        dfs(left, right - 1) + rightPile)
            return cache[(left, right)]
        return dfs(0, len(piles) - 1) > (sum(piles)) // 2

    def stoneGame2(self, piles: List[int]) -> bool:
        return True

    def stoneGame3(self, piles: List[int]) -> bool:
        n = len(piles)
        # left: from n-1 to 0 (n kinds)
        # right: from 0 ~ n-1 (n kinds)
        
        dp = [[0] * (n+1) for _ in range(n+1)]
        for left in range(n-1, -1, -1):
            for right in range(1, n):
                # check if this round is Alice or Bob
                isAliceTurn = (right - left + 1) % 2 == 0
                leftPile = piles[left] if isAliceTurn else 0
                rightPile = piles[right] if isAliceTurn else 0
                dp[left][right] = max(dp[left+1][right] + leftPile, dp[left][right-1] + rightPile)
        return dp[0][n-1] > (sum(piles)) // 2

    def stoneGame4(self, piles: List[int]) -> bool:
        n = len(piles)
        # left: from n-1 to 0 (n kinds)
        # right: from 0 ~ n-1 (n kinds)
        
        dp0 = [0] * (n+1)
        for left in range(n-1, -1, -1):
            dp1 = [0] * (n+1)
            for right in range(1, n):
                # check if this round is Alice or Bob
                isAliceTurn = (right - left + 1) % 2 == 0
                leftPile = piles[left] if isAliceTurn else 0
                rightPile = piles[right] if isAliceTurn else 0

                dp1[right] = max(dp0[right] + leftPile, dp1[right-1] + rightPile)
            dp0 = dp1
        return dp0[n-1] > (sum(piles)) // 2



# Unit Tests
funcs = [Solution().stoneGame, Solution().stoneGame2, Solution().stoneGame3, Solution().stoneGame4]

class TestStoneGame(unittest.TestCase):
    def testStoneGame1(self):
        for func in funcs:
            piles = [5,3,4,5]
            self.assertEqual(
                func(piles=piles), True)

    def testStoneGame2(self):
        for func in funcs:
            piles = [3,7,2,3]
            self.assertEqual(
                func(piles=piles), True)

if __name__ == "__main__":
    unittest.main()
