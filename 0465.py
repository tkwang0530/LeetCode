"""
465. Optimal Account Balancing
You are given an array of transactions transactions where transactions[i] = [from_i, to_i, amount_i] indicates that the person with ID = from_i gave amount_i $ to the person with ID = to_i.

Return the minimum number of transactions required to settle the debt.

Example1:
Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Example2:
Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.

Constraints:
1 <= transactions.length <= 8
transactions[i].length == 3
0 <= from_i, to_i < 12
from_i != to_i
1 <= amount_i <= 1000
"""

"""
Note:
1. DFS with backtracking: O((n-1)!) time | O(n) space - where n is the number of unique persons
ref: https://leetcode.com/problems/optimal-account-balancing/solutions/130895/recursion-logical-thinking/
"""

import unittest
import collections
from typing import List
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def buildDebts(transactions) -> List[int]:
            debtMap = collections.defaultdict(int)
            for giver, taker, amount in transactions:
                debtMap[giver] += amount
                debtMap[taker] -= amount
            
            return [amount for amount in debtMap.values()]

        debts = buildDebts(transactions)

        n = len(debts)
        def dfs(i, debts):
            while i < n and debts[i] == 0:
                i += 1
            
            if i == n:
                return 0

            minTrans = float("inf")
            for j in range(i+1, n):
                if debts[i] * debts[j] < 0:
                    debts[j] += debts[i]
                    minTrans = min(minTrans, dfs(i+1, debts) + 1)
                    debts[j] -= debts[i]
            return minTrans

        return dfs(0, debts)

# Unit Tests
funcs = [Solution().minTransfers]

class TestMinTransfers(unittest.TestCase):
    def testMinTransfers1(self):
        for func in funcs:
            transactions = [[0, 1, 10], [2, 0, 5]]
            self.assertEqual(func(transactions=transactions), 2)

    def testMinTransfers2(self):
        for func in funcs:
            transactions = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]
            self.assertEqual(func(transactions=transactions), 1)

    def testMinTransfers3(self):
        for func in funcs:
            transactions = [[0, 1, 5], [0, 2, 5], [3, 4, 5], [3, 5, 5]]
            self.assertEqual(func(transactions=transactions), 4)


if __name__ == "__main__":
    unittest.main()
