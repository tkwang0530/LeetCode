"""
1140. Stone Game II
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

Example2:
Input: piles = [1,2,3,4,5,100]
Output: 104

Constraints:
1 <= piles.length <= 100
1 <= piles[i] <= 10^4
"""

"""
Note:
1. dfs + memo: O(n^2) time | O(n^2) space
"""

from typing import List
class Solution(object):
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        preSum = piles[:]
        for i in range(n-2, -1, -1):
            preSum[i] += preSum[i+1]

        # memo[(p, m)] stores the maximum numbers of stones player can get, with p(min available index) and m
        memo = {}
        def dfs(p, m):
            if p + 2 * m >= n:
                return preSum[p]
            
            if (p, m) in memo:
                return memo[(p, m)]
            maxVal = 0
            for x in range(1, 2*m + 1):
                # the player take x piles, total take "take" stones
                take = preSum[p] - preSum[p+x]

                # the other player's max take
                theOtherPlayerMaxTake = dfs(p+x, max(x, m))

                leftStone = preSum[p+x] - theOtherPlayerMaxTake
                nextTake = take + leftStone
                maxVal = max(maxVal, nextTake)
            memo[(p, m)] = maxVal
            return memo[(p, m)]
        return dfs(0, 1)

# Unit Tests
import unittest
funcs = [Solution().stoneGameII]

class TestStoneGame(unittest.TestCase):
    def testStoneGame1(self):
        for func in funcs:
            piles = [2,7,9,4,4]
            self.assertEqual(func(piles=piles), 10)

    def testStoneGame2(self):
        for func in funcs:
            piles = [1,2,3,4,5,100]
            self.assertEqual(func(piles=piles), 104)

if __name__ == "__main__":
    unittest.main()
