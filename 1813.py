"""
1813. Sentence Similarity III
description: https://leetcode.com/problems/sentence-similarity-iii/description/ 
"""

"""
Note:
1. Two Pointers: O(m+n) time | O(m+n) space - where m is the length of string sentence1 and n is the length of string sentence2
"""

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        short, long = sorted([sentence1, sentence2], key=len)
        words1, words2 = short.split(" "), long.split(" ")
        L1, R1 = 0, len(words1)-1 # short
        L2, R2 = 0, len(words2)-1 # long
        while L1 <= R1 and words1[L1] == words2[L2]:
            L1 += 1
            L2 += 1
        
        while L1 <= R1 and words1[R1] == words2[R2]:
            R1 -= 1
            R2 -= 1
        
        return L1 > R1

funcs = [Solution().areSentencesSimilar]

import unittest
class TestAreSentencesSimilar(unittest.TestCase):
    def testAreSentencesSimilar1(self):
        for func in funcs:
            sentence1 = "My name is Haley"
            sentence2 = "My Haley"
            self.assertEqual(func(sentence1=sentence1, sentence2=sentence2), True)

    def testAreSentencesSimilar2(self):
        for func in funcs:
            sentence1 = "of"
            sentence2 = "A lot of words"
            self.assertEqual(func(sentence1=sentence1, sentence2=sentence2), False)

if __name__ == "__main__":
    unittest.main()
