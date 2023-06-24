"""
714. Best Time to Buy and Sell Stock with Transaction Fee
You are given an array prices where prices[i] is the price of a given stock on the i-th day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transaction as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Constraints:
1 <= prices.length <= 5 * 10^4
1 <= prices[i] < 5 * 10^4
0 <= fee < 5 * 10^4
"""

"""
Note:
1. DP: O(n) time | O(1) space - where n is the length of array prices
"""

import unittest
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        idle = 0 # T[i=-1][k][0]
        hold = -float("inf") # T[i=-1][k][1]

        for price in prices:
            hold = max(hold, idle - price)
            idle = max(idle, hold + price - fee)

        return idle

# Unit Tests
import unittest
funcs = [Solution().maxProfit]
class TestMaxProfit(unittest.TestCase):
    def testMaxProfit1(self):
        for func in funcs:
            prices = [1,3,2,8,4,9]
            fee = 2
            self.assertEqual(func(prices=prices, fee=fee), 8)

    def testMaxProfit2(self):
        for func in funcs:
            prices = [1,3,7,5,10,3]
            fee = 3
            self.assertEqual(func(prices=prices, fee=fee), 6)

if __name__ == "__main__":
    unittest.main()
