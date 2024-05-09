
"""
1002. Find Common Characters
description: https://leetcode.com/problems/find-common-characters/description/
"""

"""
Note:
1. Counter: O(n) time | O(n) space - where n is the number of characters in words 
"""

from typing import List
import collections
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commonCounter = collections.Counter(words[0])
        for i in range(1, len(words)):
            word = words[i]
            commonCounter &= collections.Counter(word)

        output = []
        for char, count in commonCounter.items():
            output.extend([char]*count)

        return output

# Unit Tests
import unittest
funcs = [Solution().commonChars]

class TestCommonChars(unittest.TestCase):
    def testCommonChars1(self):
        for commonChars in funcs:
            words = ["bella","label","roller"]
            self.assertEqual(sorted(commonChars(words=words)), sorted(["e","l","l"]))

    def testCommonChars2(self):
        for commonChars in funcs:
            words = ["cool","lock","cook"]
            self.assertEqual(sorted(commonChars(words=words)), sorted(["c","o"]))

if __name__ == "__main__":
    unittest.main()