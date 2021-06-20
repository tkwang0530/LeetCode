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
1. Hash Table: O(n) time | O(1) space
2. Hash Table (rewrite): O(n) time | O(1) space
"""


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


# Unit Tests
import unittest


class TestisAnagram(unittest.TestCase):
    def testIsAnagram1(self):
        func = Solution().isAnagram
        func2 = Solution().isAnagram2
        self.assertEqual(func(s="anagram", t="nagaram"), True)
        self.assertEqual(func2(s="anagram", t="nagaram"), True)

    def testIsAnagram2(self):
        func = Solution().isAnagram
        func2 = Solution().isAnagram2
        self.assertEqual(func(s="rat", t="car"), False)
        self.assertEqual(func2(s="rat", t="car"), False)


if __name__ == "__main__":
    unittest.main()