"""
2000. Reverse Prefix of Word
description: https://leetcode.com/problems/reverse-prefix-of-word/description/
"""

"""
Note:
1. One Pass: O(n) time | O(1) space
"""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, char in enumerate(word):
            if char == ch:
                return word[:i+1][::-1]+word[i+1:]
        return word

# Unit Tests
import unittest
funcs = [Solution().reversePrefix]

class TestReversePrefix(unittest.TestCase):
    def testReversePrefix1(self):
        for func in funcs:
            word = "abcdefd"
            ch = "d"
            self.assertEqual(func(word=word, ch=ch), "dcbaefd")

    def testReversePrefix2(self):
        for func in funcs:
            word = "xyxzxe"
            ch = "z"
            self.assertEqual(func(word=word, ch=ch), "zxyxxe")

    def testReversePrefix3(self):
        for func in funcs:
            word = "abcd"
            ch = "z"
            self.assertEqual(func(word=word, ch=ch), "abcd")


if __name__ == "__main__":
    unittest.main()