"""
1576. Replace All ?'s to Avoid Consecutive Repeating Characters
description: https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/description/
"""

"""
Note:
1. Brute-Force: O(n) time | O(n) space - where n is the length of string s
"""

import unittest
class Solution:
    def modifyString(self, s: str) -> str:
        chars = list(s)
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i, char in enumerate(chars):
            if char != "?":
                continue

            leftChar = "*" if i == 0 else chars[i-1]
            rightChar = "*" if i == len(chars)-1 else chars[i+1]
            replaceChar = ""
            for alphabet in alphabets:
                if alphabet not in (leftChar, rightChar):
                    replaceChar = alphabet
                    break
            chars[i] = replaceChar
        return "".join(chars)

# Unit Tests
funcs = [Solution().modifyString]


class TestModifyString(unittest.TestCase):
    def testModifyString1(self):
        for modifyString in funcs:
            s = "?zs"
            self.assertEqual(modifyString(s=s), "azs")

    def testModifyString2(self):
        for modifyString in funcs:
            s = "ubv?w"
            self.assertEqual(modifyString(s=s), "ubvaw")


if __name__ == "__main__":
    unittest.main()
