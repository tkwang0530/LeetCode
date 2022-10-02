"""
746. Min Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost of i-th step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""

"""
Note:
1. DP: O(n) time | O(1) space - where n is the length of array cost
"""




import unittest
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        cost.append(0)
        n = len(cost)
        for i in range(2, n):
            prevCost2 = cost[i-2]
            prevCost1 = cost[i-1]
            cost[i] += min(prevCost2, prevCost1)
        return cost[-1]


# Unit Tests
funcs = [Solution().minCostClimbingStairs]


class TestMinCostClimbingStairs(unittest.TestCase):
    def testMinCostClimbingStairs1(self):
        for func in funcs:
            cost = [10, 15, 20]
            self.assertEqual(func(cost=cost), 15)

    def testMinCostClimbingStairs2(self):
        for func in funcs:
            cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
            self.assertEqual(func(cost=cost), 6)


if __name__ == "__main__":
    unittest.main()
