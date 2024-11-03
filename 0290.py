"""
290. Word Pattern
description: https://leetcode.com/problems/word-pattern/description/ 
"""

"""
Note:
1. HashMap: O(m + n) time | O(256) space - where m is the length of string pattern and n is the length of string s 
"""

import collections
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        lastSeenP = collections.defaultdict(lambda: -1)
        lastSeenWord = collections.defaultdict(lambda: -1)
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            if lastSeenP[char] != lastSeenWord[word]:
                return False

            lastSeenP[char] = i
            lastSeenWord[word] = i
        return True

# Unit Tests
import unittest
funcs = [Solution().wordPattern]

class TestWordPattern(unittest.TestCase):
    def testWordPattern1(self):
        for func in funcs:
            pattern = "abba"
            s = "dog cat cat dog"
            self.assertEqual(func(pattern=pattern, s=s), True)

    def testWordPattern2(self):
        for func in funcs:
            pattern = "abba"
            s = "dog cat cat fish"
            self.assertEqual(func(pattern=pattern, s=s), False)

    def testWordPattern3(self):
        for func in funcs:
            pattern = "aaaa"
            s = "dog cat cat dog"
            self.assertEqual(func(pattern=pattern, s=s), False)

if __name__ == "__main__":
    unittest.main()
