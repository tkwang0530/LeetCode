"""
1690. Stone Game VII
description: https://leetcode.com/problems/stone-game-vii/description/
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

class Solution2(object):
    def stoneGameVII(self, stones: List[int]) -> int:
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

class Solution3(object):
    def stoneGameVII(self, stones: List[int]) -> int:
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
funcs = [Solution().stoneGameVII, Solution2().stoneGameVII, Solution3().stoneGameVII]

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
