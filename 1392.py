"""
1392. Longest Happy Prefix
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

Example1:
Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

Example2:
Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.

Constraints:
1 <= s.length <= 10^5
s contains only lowercase English letters.
"""

""" 
1. KMP: O(n) time | O(n) space - where n is the length of string s
"""

from typing import List
class Solution(object):
    def longestPrefix(self, s: str) -> str:
        def build(p: str) -> List[int]:
            m = len(p)
            next = [0, 0]
            j = 0
            for i in range(1, m):
                while j > 0 and p[i] != p[j]:
                    j = next[j]
                if p[i] == p[j]:
                    j += 1
                next.append(j)
            return next
        next = build(s)
        print(next)
        return s[0:next[-1]]

# Unit Tests
import unittest
funcs = [Solution().longestPrefix]

class TestLongestPrefix(unittest.TestCase):
    def testLongestPrefix1(self):
        for func in funcs:
            s = "level"
            self.assertEqual(func(s=s), "l")

    def testLongestPrefix2(self):
        for func in funcs:
            s = "ababab"
            self.assertEqual(func(s=s), "abab")

    def testLongestPrefix3(self):
        for func in funcs:
            s = "bba"
            self.assertEqual(func(s=s), "")

if __name__ == "__main__":
    unittest.main()
