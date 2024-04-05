"""
1544. Make The String Great
description: https://leetcode.com/problems/make-the-string-great/description
"""

"""
Note:
1. stack: O(n) time | O(n) space - where n is the length of string s
"""

import unittest
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
            while len(stack) >= 2 and (stack[-2].lower() == stack[-1].lower()) and stack[-2] != stack[-1]:
                stack.pop()
                stack.pop()

        return "".join(stack)
    
# Unit Tests
funcs = [Solution().makeGood]


class TestMakeGood(unittest.TestCase):
    def testMakeGood1(self):
        for func in funcs:
            s = "leEeetcode"
            self.assertEqual(func(s=s), "leetcode")

    def testMakeGood2(self):
        for func in funcs:
            s = "abBAcC"
            self.assertEqual(func(s=s), "")

    def testMakeGood3(self):
        for func in funcs:
            s = "s"
            self.assertEqual(func(s=s), "s")

if __name__ == "__main__":
    unittest.main()
