"""
772. Basic Calculator III
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty space.

The expression string contains only non-negative integers, "+", "-", "*", "/" operators, open and closing parenttheses and empty spaces. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31-1].

Example1:
Input: s = "1 + 1"
Output: 2

Example2:
Input: s = "  6-4 / 2 "
Output: 4

Example3:
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21

Example4:
Input: s = "(2+6* 3+5- (3*14/7+2)*5)+3"
Output: -12
"""

"""
Note:
1. Using Stack: O(n^2) time | O(n) space
"""

class Solution(object):
    def calculate(self, s: str) -> int:
        stack = []
        currNum = 0
        sign = "+"
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                currNum = currNum * 10 + (ord(char) - ord("0"))
            if char == "(":
                left = 1
                j = i + 1
                while left > 0:
                    if s[j] == "(":
                        left += 1
                    elif s[j] == ")":
                        left -= 1
                    j += 1
                currNum = self.calculate(s[i+1: j])
                i = j - 1

            if char != " " and not char.isdigit() or i == len(s) - 1:
                if sign == "+":
                    stack.append(currNum)
                elif sign == "-":
                    stack.append(-currNum)
                elif sign == "*":
                    stack.append(stack.pop() * currNum)
                elif sign == "/":
                    stack.append(int(stack.pop() / currNum))
                sign = char
                currNum = 0
            i += 1
        return sum(stack)



# Unit Tests
import unittest
funcs = [Solution().calculate]


class TestCalculate(unittest.TestCase):
    def testCalculate1(self):
        for func in funcs:
            s = "1 + 1"
            self.assertEqual(func(s=s), 2)

    def testCalculate2(self):
        for func in funcs:
            s = "  6-4 / 2 "
            self.assertEqual(func(s=s), 4)

    def testCalculate3(self):
        for func in funcs:
            s = "2*(5+5*2)/3+(6/2+8)"
            self.assertEqual(func(s=s), 21)

    def testCalculate4(self):
        for func in funcs:
            s = "(2+6* 3+5- (3*14/7+2)*5)+3"
            self.assertEqual(func(s=s), -12)

if __name__ == "__main__":
    unittest.main()
