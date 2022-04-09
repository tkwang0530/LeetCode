"""
856. Score of Parentheses
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:
- "()" has score 1.
- "AB" has score A + B, where A and B are balanced parentheses strings.
- (A) has score 2 * A, where A is a balanced parentheses string.

Example1:
Input: s = "()"
Output: 1

Example2:
Input: s = "(())"
Output: 2

Example3:
Input: s = "()()"
Output: 2

Constraints:
2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
"""

""" 
1. Stack: O(n) time | O(n) space
"""
class Solution(object):
    def scoreOfParentheses(self, s: str) -> int:
        currentScore = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
                continue
            
            if stack[-1] == "(":
                stack[-1] = 1
                continue
            
            currentScore = 0
            while stack and stack[-1] != "(":
                currentScore += stack.pop()
            stack[-1] = currentScore * 2
            
        return sum(stack)


# Unit Tests
import unittest
funcs = [Solution().scoreOfParentheses]


class TestScoreOfParentheses(unittest.TestCase):
    def testScoreOfParentheses1(self):
        for func in funcs:
            s = "()"
            self.assertEqual(func(s=s), 1)

    def testScoreOfParentheses2(self):
        for func in funcs:
            s = "(())"
            self.assertEqual(func(s=s), 2)
    
    def testScoreOfParentheses3(self):
        for func in funcs:
            s = "()()"
            self.assertEqual(func(s=s), 2)

if __name__ == "__main__":
    unittest.main()
