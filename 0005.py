"""
5. Longest Palindromic Substring
description: https://leetcode.com/problems/longest-palindromic-substring/description/
"""

"""
Note:
1. Two Pointers 1: O(n^2) time | O(1+n) space
2. Two Pointers 2: O(n^2) time | O(n) space
3. dp: O(n^2) time | O(n^2) space
ref: https://leetcode.com/problems/longest-palindromic-substring/solutions/4212564/beats-96-49-5-different-approaches-brute-force-eac-dp-ma-recursion
"""

import unittest
class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        currentLongest = [0, 0]  # [leftIdx, rightIdx]
        for i in range(1, len(s)):
            odd = self.getLongestPalindromeFrom(s, i - 1, i + 1)
            even = self.getLongestPalindromeFrom(s, i - 1, i)
            longest = max(odd, even, key=lambda x: x[1] - x[0])
            currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
        return s[currentLongest[0]: currentLongest[1] + 1]

    def getLongestPalindromeFrom(self, s, leftIdx, rightIdx):
        while leftIdx >= 0 and rightIdx < len(s):
            if s[leftIdx] != s[rightIdx]:
                break
            leftIdx -= 1
            rightIdx += 1

        return [leftIdx + 1, rightIdx - 1]  # [1 , 0]
    
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expansionOdd(i):
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        def expansionEven(i):
            left, right = i, i+1
            if right == n or s[left] != s[right]:
                return ""

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ""
        for i in range(n):
            longest = max(
                expansionOdd(i),
                expansionEven(i),
                longest,
                key = lambda x: len(x)
            )
        return longest
    
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        n = len(s)
        maxLen = 1
        maxStr=s[0]

        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > maxLen:
                        maxLen = i-j+1
                        maxStr = s[j:i+1]
        return maxStr

# Unit Tests
funcs = [Solution().longestPalindrome, Solution2().longestPalindrome, Solution3().longestPalindrome]

class TestLongestPalindrome(unittest.TestCase):
    def testLongestPalindrome1(self):
        for func in funcs:
            self.assertTrue(func(s="babad") in ["aba", "bab", "bad"])

    def testLongestPalindrome2(self):
        for func in funcs:
            self.assertEqual(func(s="cbbd"), "bb")

    def testLongestPalindrome3(self):
        for func in funcs:
            self.assertEqual(func(s="a"), "a")

    def testLongestPalindrome4(self):
        for func in funcs:
            self.assertTrue(func(s="ac") in ["a","c"])


if __name__ == "__main__":
    unittest.main()
