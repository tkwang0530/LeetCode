"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '[', ']', '{', '}', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.


Examples:
    Input: s = "()"
    Output: true

    Input: s = "()[]{}"
    Output: true

    Input: s = "(]"
    Output: false
"""

"""
Note:
1. Using Stack: O(n) time | O(n) space
2. Using Stack with Hash Table: O(n) time | O(n) space
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ")" and stack.pop() != "(":
                    return False
                if char == "]" and stack.pop() != "[":
                    return False
                if char == "}" and stack.pop() != "{":
                    return False
        return len(stack) == 0

    def isValid2(self, s: str) -> bool:
        dict = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for symbol in s:
            if symbol in dict:
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                key = stack.pop()
                if dict[key] != symbol:
                    return False
        return len(stack) == 0


# Unit Tests
import unittest
funcs = [Solution().isValid]


class TestIsValid(unittest.TestCase):
    def testIsValid1(self):
        for func in funcs:
            self.assertEqual(func(s="()"), True)

    def testIsValid2(self):
        for func in funcs:
            self.assertEqual(func(s="()[]{}"), True)

    def testIsValid3(self):
        for func in funcs:
            self.assertEqual(func(s="(]"), False)

    def testIsValid4(self):
        for func in funcs:
            self.assertEqual(func(s="([)]"), False)

    def testIsValid5(self):
        for func in funcs:
            self.assertEqual(func(s="{[]}"), True)


if __name__ == "__main__":
    unittest.main()