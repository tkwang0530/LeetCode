"""
1347. Minimum Number of Steps to Make Two Strings Anagram
description: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description
"""

"""
Note:
1. Counter: O(m+n+26) time | O(26) space - where m and n are the lengths of the input strings
"""

import collections
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCounter = collections.Counter(s)
        tCounter = collections.Counter(t)

        diffs = 0
        for i in range(26):
            char = chr(ord("a")+i)
            diffs += abs(sCounter[char]-tCounter[char])
        
        return diffs // 2


# Unit Tests
import unittest
funcs = [Solution().minSteps]

class TestMinSteps(unittest.TestCase):
    def testMinSteps1(self):
        for func in funcs:
            s = "bab"
            t = "aba"
            self.assertEqual(func(s=s, t=t), 1)

    def testMinSteps2(self):
        for func in funcs:
            s = "leetcode"
            t = "practice"
            self.assertEqual(func(s=s, t=t), 5)

    def testMinSteps3(self):
        for func in funcs:
            s = "anagram"
            t = "mangaar"
            self.assertEqual(func(s=s, t=t), 0)

if __name__ == "__main__":
    unittest.main()