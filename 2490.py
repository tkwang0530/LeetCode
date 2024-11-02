"""
2490. Circular Sentence
description: https://leetcode.com/problems/circular-sentence/description/
"""

"""
Note:
1. One pass: O(n) time | O(n) space - where n is the length of string sentence
"""

import unittest
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        tail = sentence[-1][-1]
        for word in words:
            newHead = word[0]
            newTail = word[-1]
            if tail != newHead:
                return False
            tail = newTail
        return True

# Unit Tests
funcs = [Solution().isCircularSentence]

class TestIsCircularSentence(unittest.TestCase):
    def testIsCircularSentence1(self):
        for func in funcs:
            sentence = "leetcode exercises sound delightful"
            self.assertEqual(func(sentence=sentence), True)

    def testIsCircularSentence2(self):
        for func in funcs:
            sentence = "eetcode"
            self.assertEqual(func(sentence=sentence), True)

    def testIsCircularSentence3(self):
        for func in funcs:
            sentence = "Leetcode is cool"
            self.assertEqual(func(sentence=sentence), False)


if __name__ == "__main__":
    unittest.main()
