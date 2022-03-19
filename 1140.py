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
2. dp: O(n^2) time | O(n^2) space
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

    def stoneGameII2(self, piles: List[int]) -> int:
        n = len(piles)
        preSum = piles[:]
        for i in range(n-2, -1, -1):
            preSum[i] += preSum[i+1]

        # dp[p][m] stores the maximum numbers of stones player can get, with p(min available index) and m
        # p => 0~n
        # m => 1~n
        dp = [[0] * (n+1) for _ in range(n+1)]
        for p in range(n, -1, -1):
            for m in range(n, 0, -1):
                if p >= n:
                    break
                maxVal = 0
                for x in range(1, 2*m+1):
                    if p+x >= n:
                        nextTake = preSum[p]
                        maxVal = max(maxVal, nextTake)
                        break

                    take = preSum[p] - preSum[p+x]
                    theOtherPlayerMaxTake = dp[p+x][max(x, m)]
                    leftStone = preSum[p+x] - theOtherPlayerMaxTake
                    nextTake = take + leftStone
                    maxVal = max(maxVal, nextTake)
                dp[p][m] = maxVal
        return dp[0][1]

# Unit Tests
import unittest
funcs = [Solution().stoneGameII, Solution().stoneGameII2]

class TestStoneGame(unittest.TestCase):
    def testStoneGame1(self):
        for func in funcs:
            piles = [2,7,9,4,4]
            self.assertEqual(func(piles=piles), 10)

    def testStoneGame2(self):
        for func in funcs:
            piles = [1,2,3,4,5,100]
            self.assertEqual(func(piles=piles), 104)

    def testStoneGame3(self):
        for func in funcs:
            piles = [7479,144,1852,2769,6597,3283,7696,4949,4565,5771,6092,4341,2570,5251,7544,3774,7712,471,4624,3383,5613,8761,5660,6300,4888,7755,5989,7972,4985,6664,8039,459,1970,17,360,4864,9948,9427,6779,4934,8128,8179,5193,7372,5959,180,4390,8236,1405,59,7368,7387,2500,8028,8809,4089,8068,5640,352,5167,6863,4307,8793,2837,6903,813,7871,4052,4808,8383,6150,8614,1902,9819,895,3036,7213,6049,8227,1359,2342,1217,74,7681,7615,6483,7556,5120,6909,3437,7272,743,7285,4108,533,988,4448,4208,4991,9488]
            self.assertEqual(func(piles=piles), 259149)
if __name__ == "__main__":
    unittest.main()
