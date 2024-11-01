"""
1957. Delete Characters to Make Fancy String
description: https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/ 
"""

"""
Note:
1. One pass: O(n) time | O(n) space - where n is the length of string s
"""

import unittest
class Solution:
    def makeFancyString(self, s: str) -> str:
        chars = []
        for char in s:
            if len(chars) >= 2 and chars[-1] == chars[-2] == char:
                continue
            chars.append(char)

        return "".join(chars)

# Unit Tests
funcs = [Solution().makeFancyString]

class TestMakeFancyString(unittest.TestCase):
    def testMakeFancyString1(self):
        for func in funcs:
            s = "leeetcode"
            self.assertEqual(func(s=s), "leetcode")

    def testMakeFancyString2(self):
        for func in funcs:
            s = "aaabaaaa"
            self.assertEqual(func(s=s), "aabaa")

    def testMakeFancyString3(self):
        for func in funcs:
            s = "aab"
            self.assertEqual(func(s=s), "aab")


if __name__ == "__main__":
    unittest.main()
