"""
2486. Append Characters to String to Make Subsequence
description: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space - where n is the length of string s
"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t)-j

# Unit Tests
import unittest
funcs = [Solution().appendCharacters]

class TestAppendCharacters(unittest.TestCase):
    def testAppendCharacters1(self):
        for func in funcs:
            s = "coaching"
            t = "coding"
            self.assertEqual(func(s, t), 4)

    def testAppendCharacters2(self):
        for func in funcs:
            s = "abcde"
            t = "a"
            self.assertEqual(func(s, t), 0)

    def testAppendCharacters3(self):
        for func in funcs:
            s = "z"
            t = "abcde"
            self.assertEqual(func(s, t), 5)

if __name__ == "__main__":
    unittest.main()
