"""
2370. Longest Ideal Subsequence

description: https://leetcode.com/problems/longest-ideal-subsequence/description/
"""

"""
Note:
1. DFS + memo: O(n*26) time | O(n*26) space - where n is the length of the input string
ref: https://www.youtube.com/watch?v=gR1E2oLQYSY
2. DP (1D): O(n*26) time | O(26) space - where n is the length of the input string
"""

import functools
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)

        @functools.lru_cache(None)
        def dfs(i, prev) -> int:
            if i == n:
                return 0
            
            maxLen = 0
            # skip s[i]
            maxLen = max(maxLen, dfs(i+1, prev))
            # include s[i]
            if prev == "" or abs(ord(prev)-ord(s[i])) <= k:
                maxLen = max(maxLen, 1 + dfs(i+1, s[i]))
            return maxLen

        return dfs(0, "")

class Solution2:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26

        for char in s:
            digit = ord(char)-ord('a') # 0-25
            longest = 1
            for prev in range(26):
                if abs(digit-prev) <= k:
                    longest = max(longest, 1 + dp[prev])
            dp[digit] = max(dp[digit], longest)

        return max(dp)

# Unit Tests
import unittest
funcs = [Solution().longestIdealString, Solution2().longestIdealString]

class TestLongestIdealString(unittest.TestCase):
    def testLongestIdealString1(self):
        for func in funcs:
            s = "acfgbd"
            k = 2
            self.assertEqual(func(s=s, k=k), 4)

    def testLongestIdealString2(self):
        for func in funcs:
            s = "abcd"
            k = 3
            self.assertEqual(func(s=s, k=k), 4)

if __name__ == "__main__":
    unittest.main()