"""
459. Repeated Substring Pattern
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example2:
Input: s = "aba"
Output: false

Example3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.
"""

""" 
1. Brute Force: O(n^2) time | O(n) space - where n is the length of string s
2. KMP: O(n) time | O(n) space - where n is the length of string s
"""

from typing import List
class Solution(object):
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for end in range(n//2):
            if n % (end+1) > 0:
                continue
            substring = s[:end+1]
            if substring * (n // (end+1)) == s:
                return True
        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
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
        
        m = len(s)
        next = build(s)

        # m - next[m] is the length of pattern
        return next[m] and m % (m - next[m]) == 0

# Unit Tests
import unittest
funcs = [Solution().repeatedSubstringPattern, Solution().repeatedSubstringPattern2]

class TestRepeatedSubstringPattern(unittest.TestCase):
    def testRepeatedSubstringPattern1(self):
        for func in funcs:
            s = "abab"
            self.assertEqual(func(s=s), True)

    def testRepeatedSubstringPattern2(self):
        for func in funcs:
            s = "aba"
            self.assertEqual(func(s=s), False)

    def testRepeatedSubstringPattern3(self):
        for func in funcs:
            s = "abcabcabcabc"
            self.assertEqual(func(s=s), True)

if __name__ == "__main__":
    unittest.main()
