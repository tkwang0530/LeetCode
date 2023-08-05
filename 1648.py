"""
1648. Sell Diminishing-Valued Colored Balls
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 10^9 + 7.

Example1:
Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.

Example2:
Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.

Constraints:
1 <= inventory.length <= 10^5
1 <= inventory[i] <= 10^9
1 <= orders <= min(sum(inventory[i]), 10^9)
"""

"""
Note:
1. Greedy Algorithm: O(nlogn) time | O(n) space - where n is the length of array inventory
"""

import collections
from typing import List
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7
        inventoryCounter = collections.Counter(inventory)
        inventoryProp = []
        for key, count in inventoryCounter.items():
            inventoryProp.append([key, count])
        
        inventoryProp.sort()
        
        cost = 0
        while orders > 0:
            firstProp = inventoryProp[-1]
            hasSecond = False
            secondProp = [0, -1]
            if len(inventoryProp) >= 2:
                hasSecond = True
                secondProp = inventoryProp[-2]
            
            
            diff = firstProp[1] * firstProp[0]

            if hasSecond:
                diff = (firstProp[0]-secondProp[0]) * firstProp[1]

            diff = min(diff, orders)
            
            high = diff // firstProp[1]
            remain = diff % firstProp[1]

            cost = (cost + (firstProp[0]+firstProp[0]-high+1) * high // 2 * firstProp[1]) % MOD
            cost = (cost + (firstProp[0]-high) * remain) % MOD

            if hasSecond:
                inventoryProp[-2][1] += inventoryProp[-1][1]
            
            orders -= diff
            inventoryProp.pop()
  
        return cost

# Unit Tests
import unittest
funcs = [Solution().maxProfit]


class TestMaxProfit(unittest.TestCase):
    def testMaxProfit1(self):
        for func in funcs:
            inventory = [2,5]
            orders = 4
            self.assertEqual(func(inventory=inventory, orders=orders), 14)

    def testMaxProfit2(self):
        for func in funcs:
            inventory = [3,5]
            orders = 6
            self.assertEqual(func(inventory=inventory, orders=orders), 19)

if __name__ == "__main__":
    unittest.main()
