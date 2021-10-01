"""
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

for example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

""" 
1. 2D Dynamic Programming: O(nm) time | O(nm) space - where n is the length of text1 and m is the length of text2
dp[i][j] = dp[i+1][j+1] if text1[i] == text2[j] else max(dp[i][j+1], dp[i+1][j])
"""

class Solution(object):
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                dp[i][j] = 1 + dp[i+1][j+1] if text1[i] == text2[j] else max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

# Unit Tests
import unittest
funcs = [Solution().longestCommonSubsequence]


class TestLongestCommonSubsequence(unittest.TestCase):
    def testLongestCommonSubsequence1(self):
        for func in funcs:
            text1 = "abcde"
            text2 = "ace" 
            self.assertEqual(func(text1=text1, text2=text2), 3)

    def testLongestCommonSubsequence2(self):
        for func in funcs:
            text1 = "abc"
            text2 = "abc"
            self.assertEqual(func(text1=text1, text2=text2), 3)

    def testLongestCommonSubsequence3(self):
        for func in funcs:
            text1 = "abc"
            text2 = "def"
            self.assertEqual(func(text1=text1, text2=text2), 0)

if __name__ == "__main__":
    unittest.main()
