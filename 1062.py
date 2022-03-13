"""
1062. Longest Repeating Substring
Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.

Example1:
Input: s = "abcd"
Output: 0
Explanation: There is no repeating substring.

Example2:
Input: s = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.

Example3:
Input: s = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.

Constraints:
1 <= s.length <= 2000
s consists of lowercase English letters.
"""

"""
Note:
1. DP: O(n^2) time | O(n^2) space
dp[i][j] means # of repeated chars for substrings ending at i and j, where j > i
if s[i] != s[j]: dp[i][j] = 0; otherwise dp[i][j] = dp[i-1][j-1] + 1
2. DP (improve): O(n^2) time | O(n) space
"""

from typing import List
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n+1)]
        maxCount = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    maxCount = max(maxCount, dp[i][j])
        return maxCount

    def longestRepeatingSubstring2(self, s: str) -> int:
        n = len(s)
        dp0 = [0] * (n+1) # previous
        maxCount = 0
        for i in range(1, n+1):
            dp1 = [0] * (n+1) # current
            for j in range(i+1, n+1):
                if s[i-1] == s[j-1]:
                    dp1[j] = dp0[j-1] + 1
                    maxCount = max(maxCount, dp1[j])
            dp0 = dp1
        return maxCount

# Unit Tests
import unittest
funcs = [Solution().longestRepeatingSubstring, Solution().longestRepeatingSubstring2]

class TestLongestRepeatingSubstring(unittest.TestCase):
    def testLongestRepeatingSubstring1(self):
        for func in funcs:
            s = "abcd"
            self.assertEqual(func(s=s), 0)

    def testLongestRepeatingSubstring2(self):
        for func in funcs:
            s = "abbaba"
            self.assertEqual(func(s=s), 2)

    def testLongestRepeatingSubstring3(self):
        for func in funcs:
            s = "aabcaabdaab"
            self.assertEqual(func(s=s), 3)

    def testLongestRepeatingSubstring4(self):
        for func in funcs:
            s = "aaaaa"
            self.assertEqual(func(s=s), 4)


if __name__ == "__main__":
    unittest.main()
