"""
1249. Minimum Remove to Make Valid Parentheses
Given a string s of '(', ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercases, or
- It can be written as AB (A concatenated with B), where A an B are valid strings, or
- It can be written as (A), where A is a valid string.

Example1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

Constraints:
1 <= s.length <= 10^5
s[i] is one of '(', ')' and lowercase English letters.
"""

"""
Note:
1. Two Pass with counter: O(n) time | O(n) space
(1) from left to right: meet "(" counter++, meet ")" counter--
(2) from right to left: meet ")" counter++, meet "(" counter--
(3) if during the process counter = 0 but we still want to minus 1, then change the current position to empty string
"""




import unittest
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        counter = 0
        for i in range(len(chars)):
            if chars[i] == "(":
                counter += 1
            elif chars[i] == ")":
                if counter > 0:
                    counter -= 1
                else:
                    chars[i] = ""
        counter = 0
        for i in range(len(chars) - 1, -1, -1):
            if chars[i] == ")":
                counter += 1
            elif chars[i] == "(":
                if counter > 0:
                    counter -= 1
                else:
                    chars[i] = ""
        return "".join(chars)


# Unit Tests
funcs = [Solution().minRemoveToMakeValid]


class TestMinRemoveToMakeValid(unittest.TestCase):
    def testMinRemoveToMakeValid1(self):
        for func in funcs:
            s = "lee(t(c)o)de)"
            self.assertEqual(func(s=s), "lee(t(c)o)de")

    def testMinRemoveToMakeValid2(self):
        for func in funcs:
            s = "a)b(c)d"
            self.assertEqual(func(s=s), "ab(c)d")

    def testMinRemoveToMakeValid3(self):
        for func in funcs:
            s = "))(("
            self.assertEqual(func(s=s), "")

    def testMinRemoveToMakeValid4(self):
        for func in funcs:
            s = "(a(b(c)d)"
            self.assertEqual(func(s=s), "a(b(c)d)")

if __name__ == "__main__":
    unittest.main()
