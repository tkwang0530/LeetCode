"""
115. Distinct Subsequences
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

Example1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example2:
Input: s = "babgbag", t = "bag"
Output: 5

Constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""

"""
Notes:
1. DFS with Memoization: O(nm) time | O(nm) space - where n is the length of s and m is the length of t
(1) if s[i] == t[j]: (i+1, j+1) + (i+1, j); otherwise (i+1, j)
(2) edge cases
    if j == len(t): return 1
    if i == len(s): return 0
"""

class Solution(object):
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        return self.dfs(s, 0, t, 0, cache)
    
    def dfs(self, s, i, t, j, cache) -> int:
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if (i, j) in cache:
            return cache[(i, j)]
        if s[i] == t[j]:
            cache[(i, j)] = self.dfs(s, i+1, t, j+1, cache) + self.dfs(s, i+1, t, j, cache)
        else:
            cache[(i, j)] = self.dfs(s, i+1, t, j, cache)
        return cache[(i, j)]


# Unit Tests
import unittest
funcs = [Solution().numDistinct]

class TestNumDistinct(unittest.TestCase):
    def testNumDistinct1(self):
        for func in funcs:
            s = "rabbbit"
            t = "rabbit"
            self.assertEqual(func(s=s, t=t), 3)

    def testNumDistinct2(self):
        for func in funcs:
            s = "babgbag"
            t = "bag"
            self.assertEqual(func(s=s, t=t), 5)

if __name__ == "__main__":
    unittest.main()