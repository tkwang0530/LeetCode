"""
224. Basic Calculator
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example1:
Input: s = "1 + 1"
Output: 2

Example2:
Input: s = " 2-1 + 2 "
Output: 3

Example3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:
1 <= s.length <= 3 * 10^5
s consists of digits and '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation
'-' could be used as a unary operation but it has to be inside parentheses.
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""

"""
Note:
1. Using Stack: O(n) time | O(n) space
where n is length of s
5 possible input we need to pay attention:
(1) digit: it should be one digit from the current number
(2) '+': number is over, we can add the previous number and start a new number
(3) '-': same as above
(4) '(': push the previous result and sign into the stack, set the result to 0, just calcuate the new result within the parenthesis.
(5) ')': pop the top two numbers from stack, first one is the sign before this pair of parenthesis, second is the temporary result before this pair of parenthesis. We add them together.
Finally return result + sign * currNum
"""




import unittest
class Solution(object):
    def calculate(self, s: str) -> int:
        stack = []
        result, sign, currNum = 0, 1, 0
        operators = {"+", "-", "(", ")"}
        digits = { str(x) for x in range(10) }
        for char in s:
            if char in digits:
                currNum = currNum * 10 + (ord(char) - ord("0"))
            if char in operators:
                if char == "+":
                    result += sign * currNum
                    sign = 1
                elif char == "-":
                    result += sign * currNum
                    sign = -1
                elif char == "(":
                    # we push the result first, then sign
                    stack.append(result)
                    stack.append(sign)

                    # reset the sign and result for the value in the parenthesis
                    result = 0
                    sign = 1
                else:
                    result += sign * currNum
                    result *= stack.pop() # stack.pop() is the sign before the open parenthesis
                    result += stack.pop() # stack.pop()  is the result calculated before parenthesis
                currNum = 0
        return result + sign * currNum



# Unit Tests
funcs = [Solution().calculate]


class TestCalculate(unittest.TestCase):
    def testCalculate1(self):
        for func in funcs:
            s = "1 + 1"
            self.assertEqual(func(s=s), 2)

    def testCalculate2(self):
        for func in funcs:
            s = " 2-1 + 2 "
            self.assertEqual(func(s=s), 3)

    def testCalculate3(self):
        for func in funcs:
            s = "(1+(4+5+2)-3)+(6+8)"
            self.assertEqual(func(s=s), 23)

if __name__ == "__main__":
    unittest.main()
