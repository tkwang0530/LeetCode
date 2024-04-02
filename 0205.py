"""
205. Isomorphic Strings
description: https://leetcode.com/problems/isomorphic-strings/description
"""

"""
Note:
1. HashMap: O(n) time | O(256) space - where n is the length of string s
"""

import collections
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCounter = collections.defaultdict(lambda: -1)
        tCounter = collections.defaultdict(lambda: -1)

        for i in range(len(s)):
            if sCounter[s[i]] != tCounter[t[i]]:
                return False

            sCounter[s[i]] = i
            tCounter[t[i]] = i
        return True

# Unit Tests
import unittest
funcs = [Solution().isIsomorphic]


class TestIsIsomorphic(unittest.TestCase):
    def testIsIsomorphic1(self):
        for func in funcs:
            s = "egg"
            t = "add"
            self.assertEqual(func(s=s, t=t), True)

    def testIsIsomorphic2(self):
        for func in funcs:
            s = "foo"
            t = "bar"
            self.assertEqual(func(s=s, t=t), False)

    def testIsIsomorphic3(self):
        for func in funcs:
            s = "paper"
            t = "title"
            self.assertEqual(func(s=s, t=t), True)

if __name__ == "__main__":
    unittest.main()
