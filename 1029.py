"""
1029. Two City Scheduling
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCost_i, bCost_i], the cost of flying the i-th person to city a is aCost_i, and the cost of flying the i-th person to city b is bCost_i.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Example1:
Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Example2:
Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859

Example3:
Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086

Constraints:
2 * n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCost_i, bCost_i <= 1000
"""

"""
Note:
1. Greedy: O(nlogn) time | O(n) space - where n is the length of array costs 
"""

import unittest
from typing import List
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[1] - x[0])
        n = len(costs) // 2
        total = 0
        for i, (aCost, bCost) in enumerate(costs):
            if i <= n-1:
                total += bCost
            else:
                total += aCost
        return total

# Unit Tests
import unittest
funcs = [Solution().twoCitySchedCost]
class TestTwoCitySchedCost(unittest.TestCase):
    def testTwoCitySchedCost1(self):
        for func in funcs:
            costs = [[10,20],[30,200],[400,50],[30,20]]
            self.assertEqual(func(costs=costs), 110)

    def testTwoCitySchedCost2(self):
        for func in funcs:
            costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
            self.assertEqual(func(costs=costs), 1859)

    def testTwoCitySchedCost3(self):
        for func in funcs:
            costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
            self.assertEqual(func(costs=costs), 3086)

if __name__ == "__main__":
    unittest.main()
