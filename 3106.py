"""
3106. Lexicographically Smallest String After Operations With Constraint
description: https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/description/
"""

"""
Note:
1. Greedy: O(n) time | O(n) space - where n is the length of string s
"""

from typing import List
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans = ""
        for char in s:
            cost = min(ord(char) - ord("a"), ord("z")-ord(char)+1)
            if k >= cost:
                ans += "a"
            else:
                ans += chr(ord(char)-k)
            k = max(0, k-cost)
        return ans

# Unit Tests
import unittest
funcs = [Solution().getSmallestString]

class TestGetSmallestString(unittest.TestCase):
    def testGetSmallestString1(self):
        for func in funcs:
            s = "zbbz"
            k = 3
            self.assertEqual(func(s=s, k=k), "aaaz")

    def testGetSmallestString2(self):
        for func in funcs:
            s = "xaxcd"
            k = 4
            self.assertEqual(func(s=s, k=k), "aawcd")

    def testGetSmallestString3(self):
        for func in funcs:
            s = "lol"
            k = 0
            self.assertEqual(func(s=s, k=k), "lol")

if __name__ == "__main__":
    unittest.main()
