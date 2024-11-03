"""
205. Isomorphic Strings
description: https://leetcode.com/problems/isomorphic-strings/description
"""

"""
Note:
1. HashMap: O(n) time | O(256) space - where n is the length of string s
2. Two HashMaps: O(n) time | O(256) space - where n is the length of string s
"""

import collections
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lastSeenS = collections.defaultdict(lambda: -1)
        lastSeenT = collections.defaultdict(lambda: -1)

        for i in range(len(s)):
            if lastSeenS[s[i]] != lastSeenT[t[i]]:
                return False

            lastSeenS[s[i]] = i
            lastSeenT[t[i]] = i
        return True

class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        replaceMap = {}
        useCharInVal = set()
        for i in range(len(s)):
            if s[i] not in replaceMap:
                if t[i] in useCharInVal:
                    return False
                useCharInVal.add(t[i])
                replaceMap[s[i]] = t[i]
            elif t[i] != replaceMap[s[i]]:
                return False

        return True

# Unit Tests
import unittest
funcs = [Solution().isIsomorphic, Solution2().isIsomorphic]


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
