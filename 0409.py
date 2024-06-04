"""
409. Longest Palindrome
description: https://leetcode.com/problems/longest-palindrome/description/
"""

""" 
Note:
1. HashTable: O(n) time | O(52) space
"""
import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCounter = collections.Counter(s)
        odds = sum([(1 if count % 2 else 0) for count in charCounter.values()])
        return len(s) - odds + (odds > 0)

# Unit Tests
import unittest
funcs = [Solution().longestPalindrome]

class TestLongestPalindrome(unittest.TestCase):
    def testLongestPalindrome1(self):
        for longestPalindrome in funcs:
            self.assertEqual(longestPalindrome(s = "abccccdd"), 7)

    def testLongestPalindrome2(self):
        for longestPalindrome in funcs:
            self.assertEqual(longestPalindrome(s = "a"), 1)

if __name__ == "__main__":
    unittest.main()
