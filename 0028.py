"""
28. Implement strStr()
Implement strStr().

Return the index of the first occurence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example3:
Input: haystack = "", needle = ""
Output: 0

Constraints:
0 <= haystack.length, needle.length <= 5 * 10^4
haystack and needle consist of only lower-case English characters.
"""

""" 
1. Brute Force: O(n * m) time | O(1) space - where n is the length of haystack, and m is the length of needle
2. Using String slicing: O(n * m) time | O(m) space - where n is the length of haystack, and m is the length of needle
3. KMP: O(n+m) time | O(m) space - where n is the length of haystack, and m is the length of needle
"""

from typing import List
class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not haystack: return -1
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not haystack: return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

    def strStr3(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        def build(p: str) -> List[int]:
            m = len(p)
            next = [0, 0]
            j = 0
            for i in range(1, m):
                while j > 0 and p[i] != p[j]:
                    j = next[j]
                if p[i] == p[j]:
                    j += 1
                next.append(j)
            return next
        
        def match(s: str, p: str) -> List[int]:
            n, m = len(s), len(p)
            next = build(p)
            ans = []
            j = 0
            for i in range(n):
                while j > 0 and s[i] != p[j]:
                    j = next[j]
                if s[i] == p[j]:
                    j += 1
                if j == m:
                    ans.append(i-m+1)
                    j = next[j]
            return ans
        
        matches = match(haystack, needle)
        return -1 if not matches else matches[0]


# Unit Tests
import unittest
funcs = [Solution().strStr, Solution().strStr2, Solution().strStr3]

class TestStrStr(unittest.TestCase):
    def testStrStr1(self):
        for func in funcs:
            haystack = "hello"
            needle = "ll"
            self.assertEqual(func(haystack=haystack, needle=needle), 2)

    def testStrStr2(self):
        for func in funcs:
            haystack = "aaaaa"
            needle = "bba"
            self.assertEqual(func(haystack=haystack, needle=needle), -1)

    def testStrStr3(self):
        for func in funcs:
            haystack = ""
            needle = ""
            self.assertEqual(func(haystack=haystack, needle=needle), 0)

    def testStrStr4(self):
        for func in funcs:
            haystack = "ababcaababcaabc"
            needle = "ababcaabc"
            self.assertEqual(func(haystack=haystack, needle=needle), 6)

    def testStrStr5(self):
        for func in funcs:
            haystack = "aabaaabaaac"
            needle = "aabaaac"
            self.assertEqual(func(haystack=haystack, needle=needle), 4)


if __name__ == "__main__":
    unittest.main()
