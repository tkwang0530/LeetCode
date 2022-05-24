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
        if needle == "":
            return 0

        # lps[i] indicates that for substring needle[:i], the maximum number of L such that substring needle[0:L] equals to needle[n-L:]
        # where n is the length of string needle and L <= n
        lps = [0] * len(needle)
        lpsIdx, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[lpsIdx]:
                lps[i] = lpsIdx + 1
                lpsIdx += 1
                i += 1
            elif lpsIdx == 0:
                lps[i] = 0
                i += 1
            else:
                lpsIdx = lps[lpsIdx - 1]

        i = 0 # ptr for haystack
        j = 0 # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i+1, j+1
            elif j == 0:
                i += 1
            else:
                # j-1 is the last matching index
                # e.g. lps[j-1] = 2
                # tell us that there are already 2 matches (needle[:2] == haystack[i:i+2]), so that we could compare char starting from j=2 rather than j = 0 (the brute-force approach)
                j = lps[j-1]
            
            if j == len(needle):
                return i - len(needle)
        return -1


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
