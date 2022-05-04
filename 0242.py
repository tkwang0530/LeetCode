"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and flase otherwise.

Example1:
Input: s = "anagram", t = "nagaram"
Output: true

Example2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""

"""
Note:
1. HashTable: O(n) time | O(1) space
2. HashTable2 (rewrite): O(n) time | O(1) space
3. HashTable3: O(n) time | O(1) space
"""

import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

        for char in t:
            if char not in dict:
                return False
            dict[char] -= 1
            if dict[char] < 0:
                return False
        return sum(dict.values()) == 0

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for char in s:
            dict[char] = dict.get(char, 0) + 1
        for char in t:
            dict[char] = dict.get(char, 0) - 1
            if dict[char] < 0:
                return False
        return sum(dict.values()) == 0

    def isAnagram3(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

# Unit Tests
import unittest
funcs = [Solution().isAnagram, Solution().isAnagram2, Solution().isAnagram3]
class TestisAnagram(unittest.TestCase):
    def testIsAnagram1(self):
        for func in funcs:
            self.assertEqual(func(s="anagram", t="nagaram"), True)

    def testIsAnagram2(self):
        for func in funcs:
            self.assertEqual(func(s="rat", t="car"), False)


if __name__ == "__main__":
    unittest.main()