"""
1915. Number of Wonderful Substrings
description: https://leetcode.com/problems/number-of-wonderful-substrings/description
"""

"""
Note:
1. bitmask + counter: O(10n) time | O(2^10) space
ref: https://www.youtube.com/watch?v=P6i1qj8DMZk
"""

import collections
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask = 0
        maskCounter = collections.defaultdict(int)
        maskCounter[0] = 1

        wonderfuls = 0
        for char in word:
            index = ord(char) - ord('a')
            mask ^= (1<<index)
            wonderfuls += maskCounter[mask] # all letters appears an even number of time

            # one letter appears an odd number of times
            for i in range(10):
                preMask = mask ^ (1<<i)
                wonderfuls += maskCounter[preMask]
            maskCounter[mask] += 1
        return wonderfuls

# Unit Tests
import unittest
funcs = [Solution().wonderfulSubstrings]

class TestWonderfulSubstrings(unittest.TestCase):
    def testWonderfulSubstrings1(self):
        for func in funcs:
            word = "aba"
            self.assertEqual(func(word=word), 4)


    def testWonderfulSubstrings2(self):
        for func in funcs:
            word = "aabb"
            self.assertEqual(func(word=word), 9)

    def testWonderfulSubstrings3(self):
        for func in funcs:
            word = "he"
            self.assertEqual(func(word=word), 2)

if __name__ == "__main__":
    unittest.main()