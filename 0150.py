"""
150. Evaluate Reverse Polish Notation
Evaluate the value of an arithmetric expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:
1 <= token.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

"""
Notes:
1. Using Stack: O(n) time | O(n) space
"10".isdigit() => True
"-10".isdigit() => False
"""

from typing import List
class Solution(object):
    def evalRPN(self, tokens: List[str]) -> str:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(token))
        return stack.pop()

# Unit Tests
import unittest
funcs = [Solution().evalRPN]

class TestEvalRPN(unittest.TestCase):
    def testEvalRPN1(self):
        for func in funcs:
            tokens = ["2","1","+","3","*"]
            self.assertEqual(func(tokens=tokens), 9)

    def testEvalRPN2(self):
        for func in funcs:
            tokens = ["4","13","5","/","+"]
            self.assertEqual(func(tokens=tokens), 6)

    def testEvalRPN3(self):
        for func in funcs:
            tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
            self.assertEqual(func(tokens=tokens), 22)


if __name__ == "__main__":
    unittest.main()