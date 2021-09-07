"""
241. Different Ways to Add Parentheses
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

Example1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

Constraints:
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*' .
"""

"""
Note:
1. DFS: O(2^n) time | O(2^n) space
"""

from typing import Callable, List, Dict
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        cache = {} # <expression, values>
        operations = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y
        }
        return self.ways(expression, cache, operations)

    def ways(self, expression: str, cache: Dict[str, List[int]], operations: Dict[str, Callable[[str], int]]) -> List[int]:
        if expression in cache:
            return cache[expression]
        result = []
        for i in range(len(expression)):
            char = expression[i]
            # Split the expression by an operator
            if char in operations:
                left = expression[0:i]
                right = expression[i+1:]

                # Get the solution of left/right sub-expressions
                waysOfLeft = self.ways(left, cache, operations)
                waysOfRight = self.ways(right, cache, operations)

                # Combine the solution
                for numLeft in waysOfLeft:
                    for numRight in waysOfRight:
                        result.append(operations[char](numLeft, numRight))

        # Edge case: Single number, e.g. expression = "3"
        if len(result) == 0:
            result.append(int(expression))

        cache[expression] = result
        return cache[expression]


# Unit Tests
import unittest
funcs = [Solution().diffWaysToCompute]


class TestDiffWaysToCompute(unittest.TestCase):
    def testDiffWaysToCompute1(self):
        for func in funcs:
            expression = "2-1-1"
            self.assertEqual(sorted(func(expression=expression)), sorted([0, 2]))

    def testDiffWaysToCompute2(self):
        for func in funcs:
            expression = "2*3-4*5"
            self.assertEqual(sorted(func(expression=expression)), sorted([-34, -14, -10, -10, 10]))

if __name__ == "__main__":
    unittest.main()
