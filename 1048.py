"""
1048. Longest String Chain
You are given an array of words where each word consists of lowercase English letters.

word_A is a predecessor of word_B if and only if we can insert exactly one letter anywhere in word_A without changing the order of the other characters to make it equal to word_B.

- For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
"""

""" 
1. dp + hashMap: O(n^2) time | O(n) space - where n is the number of words
"""

import collections
from typing import List
class Solution(object):
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0

        wordLengthMap = collections.defaultdict(set)
        maxWordLength = float("-inf")
        minWordLength = float("inf")
        wordMaxChainMap = {}
        for word in words:
            maxWordLength = max(maxWordLength, len(word))
            minWordLength = min(minWordLength, len(word))
            wordLengthMap[len(word)].add(word)
            wordMaxChainMap[word] = 1

        def isPredecessor(short, long):
            for i in range(len(long)):
                if short == long[:i] + long[i+1:]:
                    return True
            return False

        
        maxChainLength = 1
        for length in range(maxWordLength-1, minWordLength-1, -1):
            for currentWord in wordLengthMap[length]:
                for parentWord in wordLengthMap[length+1]:
                    if isPredecessor(currentWord, parentWord):
                        wordMaxChainMap[currentWord] = max(1+wordMaxChainMap[parentWord], wordMaxChainMap[currentWord])
                maxChainLength = max(maxChainLength, wordMaxChainMap[currentWord])
        
        return maxChainLength

    


# Unit Tests
import unittest
funcs = [Solution().longestStrChain]

class TestLongestStrChain(unittest.TestCase):
    def testLongestStrChain1(self):
        for func in funcs:
            words = ["a","b","ba","bca","bda","bdca"]
            self.assertEqual(func(words=words), 4)

    def testLongestStrChain2(self):
        for func in funcs:
            words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
            self.assertEqual(func(words=words), 5)

    def testLongestStrChain3(self):
        for func in funcs:
            words = ["abcd","dbqca"]
            self.assertEqual(func(words=words), 1)

    def testLongestStrChain4(self):
        for func in funcs:
            words = ["a","aa","aab","aabb","bbaac"]
            self.assertEqual(func(words=words), 4)
    
    def testLongestStrChain5(self):
        for func in funcs:
            words = ["a","ab","ac","bd","abc","abd","abdd"]
            self.assertEqual(func(words=words), 4)

if __name__ == "__main__":
    unittest.main()
