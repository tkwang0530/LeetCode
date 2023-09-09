"""
1563. Stone Game V
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's is initially zero.

Return the maximum score that Alice can obtain.

Example1:
Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

Example2:
Input: stoneValue = [4]
Output: 0

Constraints:
1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 10^6
"""

""" 
1. max recursion + memo (TLE): O(n^3) time | O(n^2) space - where n is the length of array stoneValue
2. dp (TLE): O(n^3) time | O(n^2) space - where n is the length of array stoneValue
3. optimized dp: O(n^2) time | O(n^2) space - where n is the length of array stoneValue
ref: https://leetcode.com/problems/stone-game-v/solutions/2709223/python-o-n-2-dp-solution-faster-than-100-1399ms/
"""

import functools
from typing import List
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + stoneValue[i-1]

        # rangeSum returns rangeSum from i to j inclusive
        def rangeSum(i, j):
            return preSums[j+1] - preSums[i]

        @functools.lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == j:
                return 0

            maxScore = 0
            # separate subarry[i:j] to [i:k-1] and [k:j]
            for k in range(i+1, j+1):
                leftSum = rangeSum(i, k-1)
                rightSum = rangeSum(k, j)
                if leftSum == rightSum:
                    maxScore = max(
                        maxScore,
                        leftSum + max(dfs(i, k-1), dfs(k, j))
                    )
                elif leftSum < rightSum:
                    maxScore = max(
                        maxScore,
                        leftSum + dfs(i, k-1)
                    )
                else:
                    maxScore = max(
                        maxScore,
                        rightSum + dfs(k, j)
                    )
            return maxScore

        return dfs(0, n-1)

class Solution2:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i - 1] + stoneValue[i - 1]
        
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                score = 0
                for k in range(i, j):
                    leftSum = preSums[k+1] - preSums[i]
                    rightSum = preSums[j+1] - preSums[k+1]
                    if leftSum < rightSum:
                        score = max(score, dp[i][k] + leftSum)
                    elif leftSum > rightSum:
                        score = max(score, dp[k+1][j] + rightSum)
                    else:
                        score = max(score, dp[i][k] + leftSum, dp[k+1][j] + rightSum)
                dp[i][j] = score
        return dp[0][n-1]

class Solution3:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[0] * n for _ in range(n)]
        maxScore = [[0] * n for _ in range(n)]

        for i in range(n):
            maxScore[i][i] = stoneValue[i]

        
        for k in range(1, n):
            mid = k
            rangeSum = stoneValue[k]
            rightSum = 0
            for i in range(k-1, -1, -1):
                # rangeSum = sum of stoneValue from i to k inclusive
                rangeSum += stoneValue[i]
                while (rightSum + stoneValue[mid]) * 2 <= rangeSum:
                    rightSum += stoneValue[mid]
                    mid -= 1

                # at this moment, rightSum + stoneValue[mid] > rangeSum
                # leftSum, stoneValue[mid], rightSum
                # check max left
                dp[i][k] = maxScore[i][mid] if rightSum * 2 == rangeSum else (0 if mid == i else maxScore[i][mid - 1])

                # check max right
                dp[i][k] = max(dp[i][k], 0 if mid == k else maxScore[k][mid + 1])

                # update maxScore
                maxScore[i][k] = max(maxScore[i][k - 1], dp[i][k] + rangeSum)
                maxScore[k][i] = max(maxScore[k][i + 1], dp[i][k] + rangeSum)
        return dp[0][n - 1]

# Unit Tests
import unittest
funcs = [Solution().stoneGameV, Solution2().stoneGameV, Solution3().stoneGameV]


class TestStoneGameV(unittest.TestCase):
    def testStoneGameV1(self):
        for func in funcs:
            stoneValue = [6,2,3,4,5,5]
            self.assertEqual(func(stoneValue=stoneValue), 18)

    def testStoneGameV2(self):
        for func in funcs:
            stoneValue = [7,7,7,7,7,7,7]
            self.assertEqual(func(stoneValue=stoneValue), 28)

    def testStoneGameV3(self):
        for func in funcs:
            stoneValue = [4]
            self.assertEqual(func(stoneValue=stoneValue), 0)

if __name__ == "__main__":
    unittest.main()
