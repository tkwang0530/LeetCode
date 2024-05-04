"""
392. is Subsequence
description: https://leetcode.com/problems/is-subsequence/description/
"""

"""
Note:
1. Two pointers: O(T) time | O(1) space - where T is the length of t
2. dfs + memo: O(ST) time | O(ST) space - where S is the length of s and T is the length of t
3. LCS: O(ST) time | O(ST) space - where S is the length of s and T is the length of t
"""




import unittest
import functools
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tIdx = 0
        sIdx = 0
        while tIdx < len(t) and sIdx < len(s):
            if t[tIdx] == s[sIdx]:
                sIdx += 1
            tIdx += 1
        return sIdx == len(s)

class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        S, T = len(s), len(t)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == S:
                return True
            elif j == T:
                return False

            isSub = False
            # not chose
            isSub = isSub or dfs(i, j+1)

            # if match, chose
            isSub = isSub or (s[i]==t[j] and dfs(i+1, j+1))
            return isSub
        return dfs(0, 0)

class Solution3:
    def isSubsequence(self, s: str, t: str) -> bool:
        charSet = set(s)
        tChars = [char for char in t if char in charSet]
        
        if len(tChars) < len(s):
            return False

        S, T = len(s), len(tChars)
        dp = [[0] * (T+1) for _ in range(S+1)]

        for i in range(1, S+1):
            for j in range(1, T+1):
                dp[i][j] = max(
                    dp[i][j], 
                    dp[i-1][j-1]+(s[i-1]==tChars[j-1]),
                    dp[i-1][j],
                    dp[i][j-1]
                )
        return dp[-1][-1] == S
# Unit Tests

funcs = [Solution().isSubsequence, Solution2().isSubsequence, Solution3().isSubsequence]


class TestIsSubsequence(unittest.TestCase):
    def testIsSubsequence1(self):
        for func in funcs:
            self.assertEqual(func(s="abc", t="ahbgdc"), True)

    def testIsSubsequence2(self):
        for func in funcs:
            self.assertEqual(func(s="axc", t="ahbgdc"), False)


if __name__ == "__main__":
    unittest.main()
