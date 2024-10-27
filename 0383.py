"""
383. Ransom Note
description: https://leetcode.com/problems/ransom-note/description/
"""

"""
Note:
1. HashMap: O(m+n) time | O(26) space - where m is the length of string ransomNote and n is the length of string magazine
"""

import unittest, collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCounter = collections.Counter(ransomNote)
        mCounter = collections.Counter(magazine)
        return rCounter == (rCounter & mCounter)

# Unit Tests
import unittest
funcs = [Solution().canConstruct]
class TestCanConstruct(unittest.TestCase):
    def testCanConstruct1(self):
        for func in funcs:
            ransomNote = "a"
            magazine = "b"
            self.assertEqual(func(ransomNote=ransomNote, magazine=magazine), False)

    def testCanConstruct2(self):
        for func in funcs:
            ransomNote = "aa"
            magazine = "ab"
            self.assertEqual(func(ransomNote=ransomNote, magazine=magazine), False)

    def testCanConstruct3(self):
        for func in funcs:
            ransomNote = "aa"
            magazine = "aab"
            self.assertEqual(func(ransomNote=ransomNote, magazine=magazine), True)

if __name__ == "__main__":
    unittest.main()
