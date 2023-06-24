"""
188. Best Time to Buy and Sell Stock IV
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:
0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""

"""
Note:
1. DP: O(n*k) time | O(k) space
critical value of k is n/2
if k >= n/2, we can extend k to positive infinity and the problem is equivalent to LC122
Otherwise,
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])
"""




from typing import List
import unittest
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices) // 2:
            hold = -float("inf")
            idle = 0
            for price in prices:
                oldIdle = idle
                idle = max(idle, hold+price)
                hold = max(hold, oldIdle-price)
            return idle
        
        T_ik0 = [0] * (k+1)
        T_ik1 = [-float("inf")] * (k+1)
        for price in prices:
            for j in range(k, 0, -1):
                T_ik0[j] = max(T_ik0[j], T_ik1[j]+price)
                T_ik1[j] = max(T_ik1[j], T_ik0[j-1]-price)
        return T_ik0[k]


# Unit Tests
funcs = [Solution().maxProfit]


class TestMaxProfit(unittest.TestCase):
    def testMaxProfit1(self):
        for func in funcs:
            k = 2
            prices = [2, 4, 1]
            self.assertEqual(func(k=k, prices=prices), 2)

    def testMaxProfit2(self):
        for func in funcs:
            k = 2
            prices = [3, 2, 6, 5, 0, 3]
            self.assertEqual(func(k=k, prices=prices), 7)


if __name__ == "__main__":
    unittest.main()
