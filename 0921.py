"""
921. Minimum Add to Make Parentheses Valid
Given a string s '(' and ')' parenthesis, we add the minimum number of parentheses ( '(' or ')', and in any positions ), so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:
- It is the empy string, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A us a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Example1:
Input: s = "())"
Output: 1

Example2:
Input: s = "((("
Output: 3

Example3:
Input: s = "()"
Output: 0

Example4:
Input: s = "()))(("
Output: 4

Note:
1. s.length <= 1000
2. s only consists of '(' and ')' characters
"""

"""
Note:
1. track open and close: O(n) time | O(1) space
"""




import unittest
class Solution(object):
    def minAddToMakeValid(self, s: str) -> int:
        open = close = 0
        for char in s:
            if char == "(":
                open += 1
            elif char == ")" and open > 0:
                open -= 1
            elif char == ")":
                close += 1
        return open + close


# Unit Tests
funcs = [Solution().minAddToMakeValid]


class TestMinAddToMakeValid(unittest.TestCase):
    def testMinAddToMakeValid1(self):
        for func in funcs:
            self.assertEqual(
                func(s="())"), 1)

    def testMinAddToMakeValid2(self):
        for func in funcs:
            self.assertEqual(
                func(s="((("), 3)

    def testMinAddToMakeValid3(self):
        for func in funcs:
            self.assertEqual(
                func(s="()"), 0)

    def testMinAddToMakeValid4(self):
        for func in funcs:
            self.assertEqual(
                func(s="()))(("), 4)


if __name__ == "__main__":
    unittest.main()
