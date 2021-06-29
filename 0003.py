"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.
Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

""" 
1. HashTable/Sliding Window: O(n) time | O(1) space
(1) Use a Hash Table to store the last indies of each characters
(2) Keep track the valid starting point. When there is a match update the starting point to (current index + 1)
"""




import unittest
class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        startIdx = 0
        longest = [0, 0]  # [startIdx, endIdx]
        for i, char in enumerate(s):
            if char in lastSeen:
                startIdx = max(startIdx, lastSeen[char] + 1)
            if longest[1] - longest[0] < i - startIdx:
                longest = [startIdx, i]
            lastSeen[char] = i
        return longest[1] - longest[0] + 1 if len(s) > 0 else 0


# Unit Tests
funcs = [Solution().lengthOfLongestSubstring]


class TestLengthOfLongestSubstring(unittest.TestCase):
    def testLengthOfLongestSubstring1(self):
        for func in funcs:
            self.assertEqual(func(s="abcabcbb"), 3)

    def testLengthOfLongestSubstring2(self):
        for func in funcs:
            self.assertEqual(func(s="bbbbb"), 1)

    def testLengthOfLongestSubstring3(self):
        for func in funcs:
            self.assertEqual(func(s="pwwkew"), 3)

    def testLengthOfLongestSubstring4(self):
        for func in funcs:
            self.assertEqual(func(s=""), 0)


if __name__ == "__main__":
    unittest.main()
