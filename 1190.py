"""
1190. Reverse Substrings Between Each Pair of Parentheses
description: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
"""

"""
Note:
1. HashTable: O(n) time | O(n) space - where n is the length of string s
ref: https://www.youtube.com/watch?v=n_pCJmg-RyU
"""

import unittest
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = {}
        stack = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                j = stack.pop()
                pair[j] = i
                pair[i] = j


        i, direction = 0, 1
        strs = []
        while i < len(s):
            if s[i] in ("(", ")"):
                i = pair[i]
                direction = -direction
            else:
                strs.append(s[i])
            i += direction
        return "".join(strs)

# Unit Tests
import unittest
funcs = [Solution().reverseParentheses]
class TestReverseParentheses(unittest.TestCase):
    def testReverseParentheses1(self):
        for func in funcs:
            s = "(abcd)"
            self.assertEqual(func(s=s), "dcba")

    def testReverseParentheses2(self):
        for func in funcs:
            s = "(u(love)i)"
            self.assertEqual(func(s=s), "iloveu")

    def testReverseParentheses3(self):
        for func in funcs:
            s = "(ed(et(oc))el)"
            self.assertEqual(func(s=s), "leetcode")

if __name__ == "__main__":
    unittest.main()
