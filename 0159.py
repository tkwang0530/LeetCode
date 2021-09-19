"""
159. Longest Substring with At Most Two Distinct Characters
Given a string s, find the length of the longest substring t that contains at most 2 distinct characters.

Example1:
Input: s = "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example2:
Input: s = "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""

""" 
Notes:
1. Sliding Window: O(n) time | O(1) space - where n is the length of s
"""

import collections
class Solution(object):
    def lengthOfLongestSubStringTwoDistinct(self, s: str) -> int:
        longest, start, end, uniques = 0, 0, 0, 0
        charCount = collections.defaultdict(int)
        while end < len(s):
            if charCount[s[end]] == 0:
                uniques += 1
            charCount[s[end]] += 1
            while uniques > 2:
                charCount[s[start]] -= 1
                if charCount[s[start]] == 0:
                    del charCount[s[start]]
                    uniques -= 1
                start += 1
            longest = max(longest, end - start + 1)
            end += 1
        return longest

# Unit Tests
import unittest
funcs = [Solution().lengthOfLongestSubStringTwoDistinct]

class TestLengthOfLongestSubStringTwoDistinct(unittest.TestCase):
    def testLengthOfLongestSubStringTwoDistinct1(self):
        for func in funcs:
            s = "eceba"
            self.assertEqual(func(s=s), 3)

    def testLengthOfLongestSubStringTwoDistinct2(self):
        for func in funcs:
            s = "ccaabbb"
            self.assertEqual(func(s=s), 5)

if __name__ == "__main__":
    unittest.main()
