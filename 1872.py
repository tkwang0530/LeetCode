"""
1690. Stone Game VIII
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, while the number of stones is more than one, they will do the following:
1. Choose an integer x > 1, and remove the leftmost x stones from the row.
2. Add the sum of the removed stones' values to the player's score.
3. Place a new stone, whose value is equal to that sum, on the left side of the row.

The game stops when only one stone is left in the row.

The score difference between Alice and Bob is (Alice's score = Bob's score).
Alice's goal is to maximize the score difference, and Bob's goal is the minimize the score difference.

Given an integer array stones of length n where stones[i] represents the value of the i-th stone from the left, return the score difference between Alice and Bob if they both play optimally

Example1:
Input: stones = [-1,2,-3,4,-5]
Output: 5
Explanation:
- Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
  value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
  the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.

Example2:
Input: stones = [7,-6,5,10,5,-2,-6]
Output: 13
Explanation:
- Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a
  stone of value 13 on the left. stones = [13].
The difference between their scores is 13 - 0 = 13.

Example3:
Input: stones = [-10,-12]
Output: -22
Explanation:
- Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her
  score and places a stone of value -22 on the left. stones = [-22].
The difference between their scores is (-22) - 0 = -22.

Constraints:
n == stones.length
2 <= n <= 10^5
-10^4 <= stones[i] <= 10^4
"""

""" 
1. max recursion: O(n^2) time | O(n) space
2. dp: O(n^2) time | O(n) space
3. dp (improved 1): O(n) time | O(n) space
4. dp (improved 2): O(n) time | O(n) space
5. dp (improved 3): O(n) time | O(1) space
"""
from typing import List
class Solution(object):
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        preSums = [0] * (n+1)

        # preSums[j] - preSums[i] = (stones[0]+stones[1]+...+stones[j-1]) - (stones[0]+stones[1]+...+stones[i-1])
        # = stones[i]+stones[i+1]+...+stones[j-1] = sum of the subarray stones [i, j) include i, exclude j
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + stones[i-1]

        memo = {}
        def dfs(index):
            if index in memo:
                return memo[index]

            if index == n - 1:
                return 0

            maxScore = -float("inf")
            for i in range(index+1, n):
                maxScore = max(maxScore, preSums[i+1] - dfs(i))
            
            memo[index] = maxScore
            return memo[index]
        return dfs(0)

    def stoneGameVIII2(self, stones: List[int]) -> int:
        n = len(stones)
        preSums = [0] * (n+1)

        # preSums[j] - preSums[i] = (stones[0]+stones[1]+...+stones[j-1]) - (stones[0]+stones[1]+...+stones[i-1])
        # = stones[i]+stones[i+1]+...+stones[j-1] = sum of the subarray stones [i, j) include i, exclude j
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + stones[i-1]

        dp = [0] * n
        for i in range(n - 2, -1, -1):
            maxScore = -float("inf")
            for j in range(i+1, n):
                maxScore = max(maxScore, preSums[j+1] - dp[j])
            dp[i] = maxScore
        return dp[0]

    def stoneGameVIII3(self, stones: List[int]) -> int:
        n = len(stones)
        preSums = [0] * (n+1)

        # preSums[j] - preSums[i] = (stones[0]+stones[1]+...+stones[j-1]) - (stones[0]+stones[1]+...+stones[i-1])
        # = stones[i]+stones[i+1]+...+stones[j-1] = sum of the subarray stones [i, j) include i, exclude j
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + stones[i-1]

        dp = [0] * n
        dp[n-2] = preSums[n] - dp[n-1]
        for i in range(n - 3, -1, -1):
            dp[i] = max(dp[i + 1], preSums[i + 2] - dp[i + 1])
        return dp[0]

    def stoneGameVIII4(self, stones: List[int]) -> int:
        n = len(stones)
        preSums = [0] * (n+1)

        # preSums[j] - preSums[i] = (stones[0]+stones[1]+...+stones[j-1]) - (stones[0]+stones[1]+...+stones[i-1])
        # = stones[i]+stones[i+1]+...+stones[j-1] = sum of the subarray stones [i, j) include i, exclude j
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + stones[i-1]

        previous = preSums[n]
        for i in range(n - 3, -1, -1):
            current = max(previous, preSums[i + 2] - previous)
            previous = current
        return previous

    def stoneGameVIII5(self, stones: List[int]) -> int:
        n = len(stones)
        currentSum = sum(stones)
        previous = currentSum
        for i in range(n - 1, 1, -1):
            currentSum -= stones[i]
            current = max(previous, currentSum - previous)
            previous = current
        return previous

# Unit Tests
import unittest
funcs = [Solution().stoneGameVIII, Solution().stoneGameVIII2, Solution().stoneGameVIII3, Solution().stoneGameVIII4, Solution().stoneGameVIII5]

class TestStoneGameVIII(unittest.TestCase):
    def testStoneGameVIII1(self):
        for func in funcs:
            stones = [-1,2,-3,4,-5]
            self.assertEqual(func(stones=stones), 5)

    def testStoneGameVIII2(self):
        for func in funcs:
            stones = [7,-6,5,10,5,-2,-6]
            self.assertEqual(func(stones=stones), 13)

    def testStoneGameVIII3(self):
        for func in funcs:
            stones = [-10,-12]
            self.assertEqual(func(stones=stones), -22)

if __name__ == "__main__":
    unittest.main()
