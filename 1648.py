"""
1648. Sell Diminishing-Valued Colored Balls
description: https://leetcode.com/problems/sell-diminishing-valued-colored-balls/description/
"""

"""
Note:
1. Greedy Algorithm: O(nlogn) time | O(n) space - where n is the length of array inventory
"""

import collections
from typing import List
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        countColorCount = collections.defaultdict(int)
        for color, count in enumerate(inventory):
            countColorCount[count] += 1


        countColorCountArr = [[count, colorCount] for count, colorCount in countColorCount.items()]
        countColorCountArr.sort(key=lambda x: x[0])

        currentOrders = orders
        revenue = 0
        while countColorCountArr and currentOrders > 0:
            secondCount = countColorCountArr[-2][0] if len(countColorCountArr) >= 2 else 0
            firstCount = price = countColorCountArr[-1][0]
            firstColorCount = countColorCountArr[-1][1]
            countDiff = firstCount - secondCount

            maxConsumeOrders = countDiff * firstColorCount
            consumeOrders = min(currentOrders, maxConsumeOrders)

            q = consumeOrders // firstColorCount
            r = consumeOrders % firstColorCount

            """
            |------------------q--------------------------|
            price + price-1 + price-2 + price-3 + ... price-q+1
            """
            currentRevenue = q * (price+price-q+1) // 2 * firstColorCount + r * (price-q)
            revenue += currentRevenue
            currentOrders -= consumeOrders

            if len(countColorCountArr) >= 2:
                countColorCountArr[-2][1] += firstColorCount

            countColorCountArr.pop()
        return revenue % (10 ** 9 + 7)

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
