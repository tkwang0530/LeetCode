"""
3110. Score of a String
description: https://leetcode.com/problems/score-of-a-string/description/
"""

"""
Note:
1. One pass: O(n) time | O(1) space - where n is the length of string s
"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        score = 0
        for i in range(1, n):
            score += abs(ord(s[i])-ord(s[i-1]))
        return score

# Unit Tests
import unittest
funcs = [Solution().scoreOfString]
class TestScoreOfString(unittest.TestCase):
    def testScoreOfString1(self):
        for scoreOfString in funcs:
            s = "hello"
            self.assertEqual(scoreOfString(s=s), 13)

    def testScoreOfString2(self):
        for scoreOfString in funcs:
            s = "zaz"
            self.assertEqual(scoreOfString(s=s), 50)

if __name__ == "__main__":
    unittest.main()
