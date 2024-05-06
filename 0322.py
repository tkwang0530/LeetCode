"""
322. Coin Change
description: https://leetcode.com/problems/coin-change/description/
"""

"""
Note:
1. BFS + caching (bottom up): O(n * amount) time | O(n* amount) space
2. DP (bottom up): O(n * amount) time | O(amount) space
3. dfs+memo: O(n * amount) time | O(n* amount) space
4. dp: O(n * amount) time | O(amount) space
"""


import functools, collections, unittest
from  typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        queue = collections.deque([(0, 0)]) # (totalCoins, runningAmount)
        visited = set()
        visited.add(0)
        while queue:
            totalCoins, runningAmount = queue.popleft()
            if runningAmount == amount:
                return totalCoins
            for coin in coins:
                nextAmount = runningAmount + coin
                if nextAmount <= amount and nextAmount not in visited:
                    visited.add(nextAmount)
                    queue.append((1+totalCoins, nextAmount))
        return -1

class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for value in range(1, amount + 1):
            for coin in coins:
                if value - coin >= 0:
                    dp[value] = min(dp[value], 1 + dp[value - coin])
        return dp[amount] if dp[amount] != amount + 1 else - 1

class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(None)
        def dfs(i: int, amount: int) -> int:
            if amount == 0:
                return 0
            
            if i == len(coins) or amount < 0:
                return float("inf")

            fewest = float("inf")
            
            # skip
            fewest = min(fewest, dfs(i+1, amount))
            
            # use
            fewest = min(fewest, 1+dfs(i, amount-coins[i]))
            
            return fewest

        output = dfs(0, amount)
        return output if output != float("inf") else -1

class Solution4:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for targetAmount in range(1, amount+1):
            for coin in coins:
                if targetAmount-coin >= 0 and dp[targetAmount-coin] != float("inf"):
                    dp[targetAmount] = min(dp[targetAmount], 1+dp[targetAmount-coin])
        
        return dp[-1] if dp[-1] != float("inf") else -1

# Unit Tests
funcs = [Solution().coinChange, Solution2().coinChange, Solution3().coinChange, Solution4().coinChange]


class TestCoinChange(unittest.TestCase):
    def testCoinChange1(self):
        for func in funcs:
            self.assertEqual(func(coins=[1, 2, 5], amount=11), 3)

    def testCoinChange2(self):
        for func in funcs:
            self.assertEqual(func(coins=[2], amount=3), -1)

    def testCoinChange3(self):
        for func in funcs:
            self.assertEqual(func(coins=[1], amount=0), 0)

    def testCoinChange4(self):
        for func in funcs:
            self.assertEqual(func(coins=[1], amount=2), 2)

    def testCoinChange5(self):
        for func in funcs:
            self.assertEqual(func(coins=[1], amount=1), 1)


if __name__ == "__main__":
    unittest.main()
