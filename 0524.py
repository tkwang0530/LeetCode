"""
524. Longest Word in Dictionary through Deleting
description: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
"""

"""
Note:
1. Two Pointers: O(mn) time | O(1) space - where m is the length of s and n is the length of dictionary
"""

from typing import List
import unittest
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubsequence(word):
            i = j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == len(word)

        output = (float("inf"), "")        
        for word in dictionary:
            if isSubsequence(word):
                output, _ = sorted([output, (-1*len(word), word)])
        return output[1]

# Unit Tests
funcs = [Solution().findLongestWord]


class TestFindLongestWord(unittest.TestCase):
    def testFindLongestWord1(self):
        for func in funcs:
            s = "abpcplea"
            dictionary = ["ale","apple","monkey","plea"]
            self.assertEqual(func(s=s, dictionary=dictionary), "apple")

    def testFindLongestWord2(self):
        for func in funcs:
            s = "abpcplea"
            dictionary = ["a","b","c"]
            self.assertEqual(func(s=s, dictionary=dictionary), "a")


if __name__ == "__main__":
    unittest.main()
