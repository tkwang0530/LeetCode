"""
1541. Minimum Insertions to Balance a Parentheses String
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
- Any left parenthesis '(' must have a corresponding two consecutive two consecutive right parenthesis '))'.
- Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
- For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.
Return the minimum number of insertions needed to make s balanced.

Example1:
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

Example2:
Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example3:
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

Constraints:
1 <= s.length <= 10^5
s consists of '(' and ')' only.
"""

"""
Note:
1. Stack: O(n) time | O(n) space - where n is the length of string s
"""




import unittest
class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        stack = []
        for char in s:
            if char == "(":
                if stack and stack[-1] == 1:
                    count += 1
                    stack.pop()
                stack.append(2)
            else:
                if not stack:
                    stack.append(2)
                    count += 1
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
        return sum(stack) + count


# Unit Tests
funcs = [Solution().minInsertions]


class TestMinInsertions(unittest.TestCase):
    def testMinInsertions1(self):
        for func in funcs:
            s = "(()))"
            self.assertEqual(func(s=s), 1)

    def testMinInsertions2(self):
        for func in funcs:
            s = "())"
            self.assertEqual(func(s=s), 0)

    def testMinInsertions3(self):
        for func in funcs:
            s = "))())("
            self.assertEqual(func(s=s), 3)


if __name__ == "__main__":
    unittest.main()
