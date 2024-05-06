"""
518. Coin Change II
description: https://leetcode.com/problems/coin-change-ii/description/
"""

"""
Note:
1. dfs + memo: O(n*amount) time | O(n*amount) space - where n is the length of coins array
2. dp: O(n*amount) time | O(amount) space - where n is the length of coins array
"""




import unittest
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}

        def dfs(amount, i):
            temp = amount
            if (amount, i) in memo:
                return memo[(amount, i)]
            if amount == 0:
                return 1
            elif i == n or amount < 0:
                return 0

            total = 0
            for used in range(amount // coins[i] + 1):
                total += dfs(amount - used*coins[i], i+1)

            memo[(temp, i)] = total
            return memo[(temp, i)]

        return dfs(amount, 0)

class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] += dp[x - coin]
        return dp[amount]


# Unit Tests
funcs = [Solution().change, Solution2().change]


class TestChange(unittest.TestCase):
    def testChange1(self):
        for func in funcs:
            amount = 5
            coins = [1, 2, 5]
            self.assertEqual(func(amount=amount, coins=coins),
                             4)

    def testChange2(self):
        for func in funcs:
            amount = 3
            coins = [2]
            self.assertEqual(func(amount=amount, coins=coins), 0)

    def testChange3(self):
        for func in funcs:
            amount = 10
            coins = [10]
            self.assertEqual(func(amount=amount, coins=coins), 1)


if __name__ == "__main__":
    unittest.main()
