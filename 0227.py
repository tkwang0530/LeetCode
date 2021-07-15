"""
227. Basic Calculator II
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example1:
Input: s = "3+2*2"
Output: 7

Example2:
Input: s = " 3/2 "
Output: 1

Example3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:
1 <= s.length <= 3 * 10^5
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

"""
Note:
1. Using Stack: O(n) time | O(n) space
using ord(char) - ord("0")  to convert string to number
"""




import unittest
class Solution(object):
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        operators = {"+", "-", "*", "/"}
        operator, currentNum, stack = "+", 0, []
        nums = set(str(num) for num in range(10))

        for idx, char in enumerate(s):
            if char in nums:
                currentNum = currentNum * 10 + (ord(char) - ord("0"))
            if char in operators or idx == len(s) - 1:
                if operator == "+":
                    stack.append(currentNum)
                elif operator == "-":
                    stack.append(-currentNum)
                elif operator == "*":
                    temp = stack.pop()
                    stack.append(temp * currentNum)
                else:
                    temp = stack.pop()
                    if temp < 0 and temp % currentNum != 0:
                        stack.append(temp // currentNum + 1)
                    else:
                        stack.append(temp // currentNum)
                operator = char
                currentNum = 0
        return sum(stack)


# Unit Tests
funcs = [Solution().calculate]


class TestCalculate(unittest.TestCase):
    def testCalculate1(self):
        for func in funcs:
            s = "3+2*2"
            self.assertEqual(func(s=s), 7)

    def testCalculate2(self):
        for func in funcs:
            s = " 3/2 "
            self.assertEqual(func(s=s), 1)

    def testCalculate3(self):
        for func in funcs:
            s = " 3+5 / 2 "
            self.assertEqual(func(s=s), 5)

    def testCalculate4(self):
        for func in funcs:
            s = " 14-3 / 2 "
            self.assertEqual(func(s=s), 13)

    def testCalculate5(self):
        for func in funcs:
            s = " 100- 10/10 "
            self.assertEqual(func(s=s), 99)


if __name__ == "__main__":
    unittest.main()
