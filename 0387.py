"""
387. First Unique Character in a String
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1

Example1:
Input: s = "leetcode"
Output: 0

Example2:
Input: s = "loveleetcode"
Output: 2

Example3:
Input: s = "aabb"
Output: -1
"""

""" 
1. Hash Table: O(n) time | O(1) space
"""




import unittest
class Solution(object):
    def firstUniqChar(self, s: str) -> int:
        alphabetCounts = {}
        for char in s:
            alphabetCounts[char] = alphabetCounts.get(char, 0) + 1

        for i in range(len(s)):
            if alphabetCounts[s[i]] == 1:
                return i
        return -1


# Unit Tests
funcs = [Solution().firstUniqChar]


class TestFirstUniqChar(unittest.TestCase):
    def testFirstUniqChar1(self):
        for func in funcs:
            self.assertEqual(func(s="leetcode"), 0)

    def testFirstUniqChar2(self):
        for func in funcs:
            self.assertEqual(func(s="loveleetcode"), 2)

    def testFirstUniqChar3(self):
        for func in funcs:
            self.assertEqual(func(s="aabb"), -1)


if __name__ == "__main__":
    unittest.main()
