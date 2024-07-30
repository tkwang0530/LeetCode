"""
1653. Minimum Deletions to Make String Balanced
description: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/
"""

"""
Note:
1. dp: O(2n) time | O(2n) space - where n is the length of string s
"""

import unittest
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [[float("inf")] * 2 for _ in range(n+1)]
        dp[-1] = [0, 0]
        for i in range(n-1, -1, -1):
            for allowA in range(2):
                char = s[i]
                if char == "a":
                    dp[i][allowA] = min(dp[i][allowA], (not allowA) + dp[i+1][allowA])

                if char == "b":
                    dp[i][allowA] = min(dp[i][allowA], dp[i+1][0])
                    if allowA:
                        dp[i][allowA] = min(dp[i][allowA], 1 + dp[i+1][allowA])
        return dp[0][1]

# Unit Tests
funcs = [Solution().minimumDeletions]

class TestMinimumDeletions(unittest.TestCase):
    def testMinimumDeletions1(self):
        for func in funcs:
            s = "aababbab"
            self.assertEqual(func(s=s), 2)

    def testMinimumDeletions2(self):
        for func in funcs:
            s = "bbaaaaabb"
            self.assertEqual(func(s=s), 2)

if __name__ == "__main__":
    unittest.main()
