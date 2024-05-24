"""
1255. Maximum Score Words Formed by Letters
description: https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/
"""

"""
Note:
1. Backtracking: O(2^n*W + L) time | O(n) space - where n is the length of array words, W is the length of the longest word, and L is the length of the letters
ref: https://www.youtube.com/watch?v=1cV8Hq9IAk4
"""

import collections
from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        letterCounter = collections.Counter(letters)

        def canFormWord(i):
            wordCounter = collections.Counter(words[i])
            for char in wordCounter.keys():
                if letterCounter[char] < wordCounter[char]:
                    return False
            return True
        
        def getScore(i):
            output = 0
            for char in words[i]:
                output += score[ord(char)-ord("a")]
            return output
        
        def backtrack(i):
            if i == n:
                return 0

            # skip
            maxScore = backtrack(i+1)

            # include (when possible)
            if canFormWord(i):
                for char in words[i]:
                    letterCounter[char] -= 1
                maxScore = max(maxScore, getScore(i) + backtrack(i+1))
                for char in words[i]:
                    letterCounter[char] += 1
            return maxScore

        return backtrack(0)

# Unit Tests
import unittest
funcs = [Solution().maxScoreWords]


class TestMaxScoreWords(unittest.TestCase):
    def testMaxScoreWords1(self):
        for maxScoreWords in funcs:
            words = ["dog","cat","dad","good"]
            letters = ["a","a","c","d","d","d","g","o","o"]
            score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
            self.assertEqual(maxScoreWords(words=words, letters=letters, score=score), 23)

    def testMaxScoreWords2(self):
        for maxScoreWords in funcs:
            words = ["xxxz","ax","bx","cx"]
            letters = ["z","a","b","c","x","x","x"]
            score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
            self.assertEqual(maxScoreWords(words=words, letters=letters, score=score), 27)

    def testMaxScoreWords3(self):
        for maxScoreWords in funcs:
            words = ["leetcode"]
            letters = ["l","e","t","c","o","d"]
            score = [0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
            self.assertEqual(maxScoreWords(words=words, letters=letters, score=score), 0)

if __name__ == "__main__":
    unittest.main()
