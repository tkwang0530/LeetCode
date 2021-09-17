"""
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example3:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
"""

"""
Note:
1. Using Stack: O(n) time | O(n) space
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        maxLength = 0
        leftMost = -1
        stack = []
        for i, char in enumerate(s):
            if char == "(":
                # if the char is open parenthese, push its index into the stack
                stack.append(i)
            else:
                # the stack is empty means the char ")"  disconnect the s from two valid substrings
                if len(stack) == 0:
                    leftMost = i
                else:
                    stack.pop()
                    maxLength = max(maxLength, i - stack[-1]) if len(stack) > 0 else max(maxLength, i-leftMost)
        return maxLength


# Unit Tests
import unittest
funcs = [Solution().longestValidParentheses]


class TestLongestValidParentheses(unittest.TestCase):
    def testLongestValidParentheses1(self):
        for func in funcs:
            s = "(()"
            self.assertEqual(func(s=s), 2)

    def testLongestValidParentheses2(self):
        for func in funcs:
            s = ")()())"
            self.assertEqual(func(s=s), 4)

    def testLongestValidParentheses3(self):
        for func in funcs:
            s = ""
            self.assertEqual(func(s=s), 0)

if __name__ == "__main__":
    unittest.main()