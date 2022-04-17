"""
1690. Stone Game VII
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stone's values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents the value of the i-th stone from the left, return the difference in Alice and Bob's score if they both play optimally.

Example1:
Input: stones = [5,3,1,4,2]
Output: 6
Explanation: 
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.

Example2:
Input: stones = [7,90,5,1,100,10,10,2]
Output: 122

Constraints:
n == stones.length
2 <= n <= 1000
1 <= stones[i] <= 1000
"""

""" 
1. max recursion: O(n^2) time | O(n^2) space
2. dp: O(n^2) time | O(n^2) space
3. dp (improved): O(n^2) time | O(n) space
"""
from typing import List
class Solution(object):
    def stoneGameVII(self, stones: List[int]) -> int:
        cache = {} # subarr of stones from index left to index right -> max Scores of player

        n = len(stones)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + stones[i-1]
        
        # return max Scores of player
        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]

            pickLeftPoint = preSums[right+1] - preSums[left+1]
            pickRightPoint = preSums[right] - preSums[left]

            cache[(left, right)] = max(pickLeftPoint - dfs(left+1, right), pickRightPoint - dfs(left, right-1))
            
            return cache[(left, right)]
        return dfs(0, len(stones) - 1)

    def stoneGameVII2(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * n for _ in range(n)]

        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + stones[i-1]
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                pickLeftPoint = preSums[j+1] - preSums[i+1]
                pickRightPoint = preSums[j] - preSums[i]

                if i + 1 < n:
                    dp[i][j] = max(dp[i][j], pickLeftPoint - dp[i+1][j])
                else:
                    dp[i][j] = max(dp[i][j], pickLeftPoint)

                if j - 1 >= 0:
                    dp[i][j] = max(dp[i][j], pickRightPoint - dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i][j], pickRightPoint)

        return dp[0][n-1]

    def stoneGameVII3(self, stones: List[int]) -> int:
        n = len(stones)
        dp0 = [0] * n

        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + stones[i-1]
        
        for i in range(n-1, -1, -1):
            dp1 = [0] * n
            for j in range(i, n):
                pickLeftPoint = preSums[j+1] - preSums[i+1]
                pickRightPoint = preSums[j] - preSums[i]

                dp1[j] = max(dp1[j], pickLeftPoint - dp0[j])

                if j - 1 >= 0:
                    dp1[j] = max(dp1[j], pickRightPoint - dp1[j-1])
                else:
                    dp1[j] = max(dp1[j], pickRightPoint)
            dp0 = dp1
        return dp0[n-1]
# Unit Tests
import unittest
funcs = [Solution().stoneGameVII, Solution().stoneGameVII2, Solution().stoneGameVII3]

class TestStoneGameVII(unittest.TestCase):
    def testStoneGameVII1(self):
        for func in funcs:
            stones = [5,3,1,4,2]
            self.assertEqual(func(stones=stones), 6)

    def testStoneGameVII2(self):
        for func in funcs:
            stones = [7,90,5,1,100,10,10,2]
            self.assertEqual(func(stones=stones), 122)

if __name__ == "__main__":
    unittest.main()
