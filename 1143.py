"""
1143. Longest Common Subsequence
description: https://leetcode.com/problems/longest-common-subsequence/description
"""

""" 
1. 2D Dynamic Programming: O(nm) time | O(nm) space - where n is the length of text1 and m is the length of text2
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0]*(l1+1) for _ in range(l2+1)]
        for idx2 in range(1, l2+1):
            for idx1 in range(1, l1+1):
                dp[idx2][idx1] = max(
                    dp[idx2-1][idx1],
                    dp[idx2][idx1-1],
                    dp[idx2-1][idx1-1] + (text1[idx1-1] == text2[idx2-1])
                )
        return dp[-1][-1]

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
