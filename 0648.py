"""
648. Replace Words
description: https://leetcode.com/problems/replace-words/description/
"""

""" 
Note:
1. HashSet: O(w * min(maxRootLen, wordLen)) time | O(r * maxRootLen) space - where w is the number of words, r is the number of roots, and maxRootLen is the maximum length of a root 
"""

from typing import List
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        maxRootLen = max([len(w) for w in dictionary])
        words = sentence.split(" ")
        n = len(words)
        output = words.copy()
        for i in range(n):
            word = words[i]
            for L in range(1, min(maxRootLen, len(word))+1):
                prefixStr = word[:L]
                if prefixStr in roots:
                    output[i] = prefixStr
                    break
        return " ".join(output)

# Unit Tests
import unittest
funcs = [Solution().replaceWords]

class TestReplaceWords(unittest.TestCase):
    def testReplaceWords1(self):
        for func in funcs:
            dictionary = ["cat","bat","rat"]
            sentence = "the cattle was rattled by the battery"
            self.assertEqual(func(dictionary=dictionary, sentence=sentence), "the cat was rat by the bat")

    def testReplaceWords2(self):
        for func in funcs:
            dictionary = ["a","b","c"]
            sentence = "aadsfasf absbs bbab cadsfafs"
            self.assertEqual(func(dictionary=dictionary, sentence=sentence), "a a b c")


if __name__ == "__main__":
    unittest.main()
