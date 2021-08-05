"""
76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
"""

""" 
1. HashTable/Sliding Window: O(n+m) time | O(1) space
"""

import unittest
class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        winStart = subStart = matched = 0
        minLength = float("inf")
        dict = {}
        for char in t:
            dict[char] = dict.get(char, 0) + 1
        for end in range(len(s)):
            endChar = s[end]
            if endChar in dict:
                dict[endChar] -= 1
                if dict[endChar] >= 0:
                    matched += 1
            while matched == len(t):
                if end - winStart + 1 < minLength:
                    minLength = end - winStart + 1
                    subStart = winStart
                startChar = s[winStart]
                if startChar in dict:
                    if dict[startChar] == 0:
                        matched -= 1
                    dict[startChar] += 1
                winStart += 1
        if minLength > len(s):
            return ""
        return s[subStart:subStart+minLength]



# Unit Tests
funcs = [Solution().minWindow]


class TestMinWindow(unittest.TestCase):
    def testMinWindow1(self):
        for func in funcs:
            s = "ADOBECODEBANC"
            t = "ABC"
            self.assertEqual(func(s=s, t=t), "BANC")

    def testMinWindow2(self):
        for func in funcs:
            s = "a"
            t = "a"
            self.assertEqual(func(s=s, t=t), "a")

    def testMinWindow3(self):
        for func in funcs:
            s = "a"
            t = "aa"
            self.assertEqual(func(s=s, t=t), "")

if __name__ == "__main__":
    unittest.main()
