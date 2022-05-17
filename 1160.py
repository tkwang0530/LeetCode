"""
1160. Find Words That Can Be Formed by Characters
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Constraints:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
"""

"""
Notes:
1. Hash Table: O(nw) time | O(1) space - where n is the length of words and w is the max word length
"""

import collections
from typing import List
class Solution(object):
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCount = collections.Counter(chars)
        totalLength = 0
        for word in words:
            wordCharCount = collections.Counter(word)
            isGood = True
            for char, count in wordCharCount.items():
                if char not in charCount or charCount[char] < count:
                    isGood = False
            if isGood:
                totalLength += len(word)
        return totalLength

# Unit Tests
import unittest
funcs = [Solution().countCharacters]

class TestCountCharacters(unittest.TestCase):
    def testCountCharacters1(self):
        for func in funcs:
            words = ["cat","bt","hat","tree"]
            chars = "atach"
            self.assertEqual(func(words=words, chars=chars), 6)

    def testCountCharacters2(self):
        for func in funcs:
            words = ["hello","world","leetcode"]
            chars = "welldonehoneyr"
            self.assertEqual(func(words=words, chars=chars), 10)

if __name__ == "__main__":
    unittest.main()