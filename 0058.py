"""
58. Length of Last Word
description: https://leetcode.com/problems/length-of-last-word/description
"""

"""
Note:
1. one pass: O(n) time | O(1) space - where n is the length of the input string
"""


from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        end = start = -1
        while i >= 0 and s[i] == " ":
            i -= 1
        
        end = i+1
        while i >= 0 and s[i] != " ":
            i -= 1
        
        start = i+1
        return end - start

# Unit Tests
import unittest
funcs = [Solution().lengthOfLastWord]


class TestLengthOfLastWord(unittest.TestCase):
    def testLengthOfLastWord1(self):
        for func in funcs:
            s = "Hello World"
            self.assertEqual(func(s=s), 5)

    def testLengthOfLastWord2(self):
        for func in funcs:
            s = "   fly me   to   the moon  "
            self.assertEqual(func(s=s), 4)

    def testLengthOfLastWord3(self):
        for func in funcs:
            s = "luffy is still joyboy"
            self.assertEqual(func(s=s), 6)

if __name__ == "__main__":
    unittest.main()
