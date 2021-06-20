"""
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
Examples:
    Given "babad", the answer is "bab". "aba" is also a valid answer.
    Given "cbbd", the answer is "bb".
    Given "a", the answer is "a". 
    Given "ac", the answer is "a". 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


class Solution(object):
    def longestPalindrome(self, s: str) -> str:  # s = "ac"
        currentLongest = [0, 0]
        for i in range(1, len(s)):
            odd = self.getLongestPalindromeFrom(s, i - 1, i + 1)
            even = self.getLongestPalindromeFrom(s, i - 1, i)
            longest = max(odd, even, key=lambda x: x[1] - x[0])
            currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
        return s[currentLongest[0] : currentLongest[1] + 1]

    def getLongestPalindromeFrom(self, s, leftIdx, rightIdx):  # "ac", 0, 1
        while leftIdx >= 0 and rightIdx < len(s):
            if s[leftIdx] != s[rightIdx]:
                break
            leftIdx -= 1
            rightIdx += 1

        return [leftIdx + 1, rightIdx - 1]  # [1 , 0]


# Unit Tests
import unittest


class TestLongestPalindrome(unittest.TestCase):
    def testLongestPalindrome1(self):
        func = Solution().longestPalindrome
        self.assertEqual(func(s="babad"), "aba")

    def testLongestPalindrome2(self):
        func = Solution().longestPalindrome
        self.assertEqual(func(s="cbbd"), "bb")

    def testLongestPalindrome3(self):
        func = Solution().longestPalindrome
        self.assertEqual(func(s="a"), "a")

    def testLongestPalindrome4(self):
        func = Solution().longestPalindrome
        self.assertEqual(func(s="ac"), "c")


if __name__ == "__main__":
    unittest.main()