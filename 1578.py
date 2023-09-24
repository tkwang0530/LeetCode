"""
1578. Minimum Time to Make Rope Colorful
description: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
"""

"""
Note:
1. Stack: O(n) time | O(n) space - where n is the length of array colors
"""

import unittest
from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack = [] # [(color, i)]
        cost = 0
        for i, color in enumerate(colors):
            stack.append((color, i))
            if stack and len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                costNew = neededTime[stack[-1][1]]
                costOld = neededTime[stack[-2][1]]
                if costNew < costOld:
                    stack.pop()
                    cost += costNew
                else:
                    stack.pop()
                    stack.pop()
                    cost += costOld
                    stack.append((color, i))
        return cost

# Unit Tests
funcs = [Solution().minCost]


class TestMinCost(unittest.TestCase):
    def testMinCost1(self):
        for minCost in funcs:
            colors = "abaac"
            neededTime = [1,2,3,4,5]
            self.assertEqual(minCost(colors=colors, neededTime=neededTime), 3)

    def testMinCost2(self):
        for minCost in funcs:
            colors = "abc"
            neededTime = [1,2,3]
            self.assertEqual(minCost(colors=colors, neededTime=neededTime), 0)

    def testMinCost3(self):
        for minCost in funcs:
            colors = "aabaa"
            neededTime = [1,2,3,4,1]
            self.assertEqual(minCost(colors=colors, neededTime=neededTime), 2)


if __name__ == "__main__":
    unittest.main()
