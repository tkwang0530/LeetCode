"""
1371. Find the Longest Substring Containing Vowels in Even Counts
description: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/
"""

"""
Note:
1. bitwise + kadane: O(n) time | O(1) space - where n is the length of string s
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        charMap = [0] * 26
        charMap[ord("a")-ord("a")] = 1 << 0
        charMap[ord("e")-ord("a")] = 1 << 1
        charMap[ord("i")-ord("a")] = 1 << 2
        charMap[ord("o")-ord("a")] = 1 << 3
        charMap[ord("u")-ord("a")] = 1 << 4

        val = 0
        firstPatternIdx = {0: -1}
        longest = 0
        for k, char in enumerate(s):
            val ^= charMap[ord(char)-ord("a")]
            if val in firstPatternIdx:
                L = k-firstPatternIdx[val]
                longest = max(longest, L) 
            else:
                firstPatternIdx[val] = k

        return longest

# Unit Tests
import unittest
funcs = [Solution().findTheLongestSubstring]
class TestFindTheLongestSubstring(unittest.TestCase):
    def testFindTheLongestSubstring1(self):
        for findTheLongestSubstring in funcs:
            s = "eleetminicoworoep"
            self.assertEqual(findTheLongestSubstring(s=s), 13)


    def testFindTheLongestSubstring2(self):
        for findTheLongestSubstring in funcs:
            s = "leetcodeisgreat"
            self.assertEqual(findTheLongestSubstring(s=s), 5)


    def testFindTheLongestSubstring3(self):
        for findTheLongestSubstring in funcs:
            s = "bcbcbc"
            self.assertEqual(findTheLongestSubstring(s=s), 6)

if __name__ == "__main__":
    unittest.main()
