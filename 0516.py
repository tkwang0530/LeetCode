"""
516. Longest Palindromic Subsequence
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
"""

""" 
1. dfs+memo: O(n^2) time | O(n^2) space - where n is the length of s

2. 2D Dynamic Programming: O(n^2) time | O(n^2) space - where n is the length of s
case0 base case: dp[i][i] = 1
case1 s[i] == s[j]: dp[i][j] == dp[i+1][j-1] + 2:
a ***** a

case2 otherwise. dp[i][j] = max(dp[i+1][j], dp[i][j-1])
ab****b
a****ab

3. 1D Dynamic Programming: O(n^2) time | O(n) space - where n is the length of s
"""

class Solution(object):
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dfs(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s[i] == s[j]:
                memo[(i, j)] = dfs(i+1, j-1) + 2
            else:
                memo[(i, j)] = max(dfs(i+1, j), dfs(i, j-1))
            return memo[(i, j)]
        return dfs(0, len(s) - 1)

    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n-length+1):
                j = i + length - 1
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

    def longestPalindromeSubseq3(self, s: str) -> int:
        dp0 = [0] * len(s) # solutions of length
        dp1= [0] * len(s) # solutions of length - 1
        dp2 = [0] * len(s) # solutions of length - 2

        for length in range(1, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if i == j:
                    dp0[i] = 1
                elif s[i] == s[j]:
                    dp0[i] = dp2[i+1] + 2
                else:
                    dp0[i] = max(dp1[i+1], dp1[i])
            dp0, dp1, dp2 = dp2, dp0, dp1
        return dp1[0]



# Unit Tests
import unittest
funcs = [Solution().longestPalindromeSubseq, Solution().longestPalindromeSubseq2, Solution().longestPalindromeSubseq3]


class TestLongestPalindromeSubseq(unittest.TestCase):
    def testLongestPalindromeSubseq1(self):
        for func in funcs:
            s = "bbbab"
            self.assertEqual(func(s=s), 4)

    def testLongestPalindromeSubseq2(self):
        for func in funcs:
            s = "cbbd"
            self.assertEqual(func(s=s), 2)

if __name__ == "__main__":
    unittest.main()
