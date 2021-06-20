"""
392. is Subsequence
Given two strings s and t, return if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example2:
Input: s = "rxc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s1, ... sk where k >= 10^9, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

"""
Note:
1. Two pointers: O(n) time | O(1) space
"""




import unittest
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tIdx = 0
        sIdx = 0
        while tIdx < len(t) and sIdx < len(s):
            if t[tIdx] == s[sIdx]:
                sIdx += 1
            tIdx += 1
        return sIdx == len(s)


# Unit Tests

funcs = [Solution().isSubsequence]


class TestIsSubsequence(unittest.TestCase):
    def testIsSubsequence1(self):
        for func in funcs:
            self.assertEqual(func(s="abc", t="ahbgdc"), True)

    def testIsSubsequence2(self):
        for func in funcs:
            self.assertEqual(func(s="axc", t="ahbgdc"), False)


if __name__ == "__main__":
    unittest.main()
