"""
1406. Stone Game III
Alice and Bob continue their games with piles of stones.  There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.

The scores of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

Example1:
Input: values = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.

Example2:
Input: values = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.

Example3:
Input: values = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.

Constraints:
1 <= stoneValue.length <= 5 * 10^4
-1000 <= stoneValue[i] <= 1000
"""

"""
Note:
1. dfs + memo: O(n) time | O(n) space
2. dp: O(n) time | O(n) space
"""

from typing import List
class Solution(object):
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        preSum = stoneValue[:]
        for i in range(n-2, -1, -1):
            preSum[i] += preSum[i+1]

        # memo[p] stores the maximum numbers of stones player can get, with p(min available index)
        memo = {}
        def dfs(p):
            if p >= n:
                return 0
            
            if p in memo:
                return memo[p]
            maxVal = float("-inf")
            for x in range(1, 3+1):
                if p+x >= n:
                    totalTake = preSum[p]
                    maxVal = max(maxVal, totalTake)
                    break

                # the player take x piles, total take "take" stones
                take = preSum[p] - preSum[p+x]

                # the other player's max take
                theOtherPlayerMaxTake = dfs(p+x)

                leftStone = preSum[p+x] - theOtherPlayerMaxTake

                totalTake = take + leftStone
                maxVal = max(maxVal, totalTake)
            memo[p] = maxVal
            return memo[p]
        
        total = preSum[0]
        aliceMaxSum = dfs(0)
        if total % 2 == 0 and aliceMaxSum == total // 2:
            return "Tie"
        return "Alice" if aliceMaxSum > total // 2 else "Bob"

    def stoneGameIII2(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        preSum = stoneValue[:]
        for i in range(n-2, -1, -1):
            preSum[i] += preSum[i+1]

        # dp[p] stores the maximum numbers of stones player can get, with p(min available index)
        dp = [0] * (n+1)
        for p in range(n, -1, -1):
            if p >= n:
                dp[p] = 0
                continue
            maxVal = float("-inf")
            for x in range(1, 3+1):
                if p+x >= n:
                    totalTake = preSum[p]
                    maxVal = max(maxVal, totalTake)
                    break
                # the player take x piles, total take "take" stones
                take = preSum[p] - preSum[p+x]

                # the other player's max take
                theOtherPlayerMaxTake = dp[p+x]

                leftStone = preSum[p+x] - theOtherPlayerMaxTake

                totalTake = take + leftStone
                maxVal = max(maxVal, totalTake)
            dp[p] = maxVal
        total = preSum[0]
        aliceMaxSum = dp[0]
        if total % 2 == 0 and aliceMaxSum == total // 2:
            return "Tie"
        return "Alice" if aliceMaxSum > total // 2 else "Bob"

# Unit Tests
import unittest
funcs = [Solution().stoneGameIII, Solution().stoneGameIII2]

class TestStoneGameIII(unittest.TestCase):
    def testStoneGameIII1(self):
        for func in funcs:
            stoneValue = [1,2,3,7]
            self.assertEqual(func(stoneValue=stoneValue), "Bob")

    def testStoneGameIII2(self):
        for func in funcs:
            stoneValue = [1,2,3,-9]
            self.assertEqual(func(stoneValue=stoneValue), "Alice")

    def testStoneGameIII3(self):
        for func in funcs:
            stoneValue = [1,2,3,6]
            self.assertEqual(func(stoneValue=stoneValue), "Tie")

    def testStoneGameIII4(self):
        for func in funcs:
            stoneValue = [-1,-2,-3]
            self.assertEqual(func(stoneValue=stoneValue), "Tie")

if __name__ == "__main__":
    unittest.main()
