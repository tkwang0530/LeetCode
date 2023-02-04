"""
518. Coin Change II
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example3:
Input: amount = 10, coins = [10]
Output: 1

Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
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

    def change2(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] += dp[x - coin]
        return dp[amount]


# Unit Tests
funcs = [Solution().change, Solution().change2]


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
