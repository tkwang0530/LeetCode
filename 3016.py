"""
3016. Minimum Number of Pushes to Type Word II
description: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/
"""

"""
Note:
1. HashTable + Sort: O(n+26) time | O(1) space - where n is the length of the input string word
"""

import collections
class Solution:
    def minimumPushes(self, word: str) -> int:
        costs = [4] * 2 + [3] * 8 + [2] * 8 + [1] * 8
        charCounter = collections.Counter(word)
        charCount = [(char, count) for char, count in charCounter.items()]
        charCount.sort(key=lambda x: -x[1])
        pushes = 0
        for _, count in charCount:
            pushes += count * costs.pop()
        return pushes

# Unit Tests
import unittest
funcs = [Solution().minimumPushes]
class TestMinimumPushes(unittest.TestCase):
    def testMinimumPushes1(self):
        for minimumPushes in funcs:
            word = "abcde"
            self.assertEqual(minimumPushes(word=word), 5)

    def testMinimumPushes2(self):
        for minimumPushes in funcs:
            word = "xyzxyzxyzxyz"
            self.assertEqual(minimumPushes(word=word), 12)

    def testMinimumPushes3(self):
        for minimumPushes in funcs:
            word = "aabbccddeeffgghhiiiiii"
            self.assertEqual(minimumPushes(word=word), 24)

if __name__ == "__main__":
    unittest.main()
