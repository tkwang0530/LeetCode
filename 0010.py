"""
10. Regular Expression Matching
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false

Constraints:
1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*' .
It is guaranteed for each appearance of the character '*', where will be a previous valid character to match.
"""

"""
Note:
1. DFS with memoization: O(m * n) time | O(m * n) space - where m is the length of s and n is the length of p
"""


import unittest
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # TOP-Down Memoization
        cache = {}
        return self.dfs(s, p, 0, 0, cache)

    def dfs(self, s: str, p: str, i: int, j: int, cache) -> bool:
        if (i, j) in cache:
            return cache[(i, j)]
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False
        
        match = i < len(s) and (s[i] == p[j] or p[j] == ".")
        if j+1 < len(p) and  p[j + 1] == "*":
            # don't use *      and      use *
            cache[(i, j)] = self.dfs(s, p, i, j+2, cache)  or (match and self.dfs(s, p, i+1, j, cache))
            return cache[(i, j)]
        if match:
            cache[(i, j)] =  self.dfs(s, p, i+1, j+1, cache)
            return cache[(i, j)]
        
        cache[(i, j)] = False
        return cache[(i, j)]
            



# Unit Tests
funcs = [Solution().isMatch]


class TestIsMatch(unittest.TestCase):
    def testIsMatch1(self):
        for func in funcs:
            s = "aa"
            p = "a"
            self.assertEqual(func(s=s,p=p), False)

    def testIsMatch2(self):
        for func in funcs:
            s = "aa"
            p = "a*"
            self.assertEqual(func(s=s,p=p), True)

    def testIsMatch3(self):
        for func in funcs:
            s = "ab"
            p = ".*"
            self.assertEqual(func(s=s,p=p), True)

    def testIsMatch4(self):
        for func in funcs:
            s = "aab"
            p = "c*a*b"
            self.assertEqual(func(s=s,p=p), True)

    def testIsMatch5(self):
        for func in funcs:
            s = "mississippi"
            p = "mis*is*p*."
            self.assertEqual(func(s=s,p=p), False)


if __name__ == "__main__":
    unittest.main()
