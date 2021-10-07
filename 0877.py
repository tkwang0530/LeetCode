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
"""

import unittest
from typing import List, Dict
class Solution(object):
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {} # subarr piles (left, right) -> Max Alice Total
        return self.dfs(piles, 0, len(piles) - 1, cache) > (sum(piles)) // 2
    
    def dfs(self, piles: List[int], left: int, right: int, cache: Dict) -> int:
        if left > right:
            return 0
        if (left, right) in cache:
            return cache[(left, right)]
        
        even = (right - left + 1) % 2 == 0
        leftPile = piles[left] if even else 0
        rightPile = piles[right] if even else 0
        if even:
            cache[(left, right)] = max(self.dfs(piles, left + 1, right, cache) + leftPile,
                    self.dfs(piles, left, right - 1, cache) + rightPile)
        else:
            cache[(left, right)] = min(self.dfs(piles, left + 1, right, cache) + leftPile,
                    self.dfs(piles, left, right - 1, cache) + rightPile)
        return cache[(left, right)]

    def stoneGame2(self, piles: List[int]) -> bool:
        return True


# Unit Tests
funcs = [Solution().stoneGame, Solution().stoneGame2]

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
