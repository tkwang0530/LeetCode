"""
916. Word Subsets
You are given two string arrays words1 and words2.
A string b is a subset of string a if every letter in b occurs in a including multiplicity.
- For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from "words1" is universal if for every string b in "word2", "b" is a subset of "a".

Return an array of all the universal strings in "words1". You may return the answer in any order.

Example1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

Constraints:
1 <= words1.length, word2.length <= 10^4
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""

"""
Note:
1. Counter: O(N+M) time | O(n+m) space
where
- N is the total number of  characters in words1
- M is the  total number of characters in words2
- n = len(words1)
- m = len(words2)
"""




from typing import List
import unittest
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            charCount = [0] * 26
            for letter in word:
                charCount[ord(letter) - ord("a")] += 1
            return charCount

        word2Max = [0] * 26
        for word in words2:
            for i, val in enumerate(count(word)):
                word2Max[i] = max(word2Max[i], val)

        universals = []
        for word in words1:
            if all(x >= y for x, y in zip(count(word), word2Max)):
                universals.append(word)
        return universals


# Unit Tests
funcs = [Solution().wordSubsets]


class TestWordSubsets(unittest.TestCase):
    def testWordSubsets1(self):
        for func in funcs:
            words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
            words2 = ["e", "o"]
            self.assertEqual(func(words1=words1, words2=words2), [
                             "facebook", "google", "leetcode"])

    def testWordSubsets2(self):
        for func in funcs:
            words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
            words2 = ["l", "e"]
            self.assertEqual(func(words1=words1, words2=words2), [
                             "apple", "google", "leetcode"])


if __name__ == "__main__":
    unittest.main()
