"""
916. Word Subsets
description: https://leetcode.com/problems/word-subsets/description/
"""

"""
Note:
1. Counter: O(n+m) time | O(n+m) space - where n is the length of words1 and m is the length of words2
"""




from typing import List
import unittest
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = [0] * 26
        for word in words2:
            tempCounter = [0] * 26
            for char in word:
                tempCounter[ord(char)-ord("a")] += 1
            for i in range(26):
                counter[i] = max(counter[i], tempCounter[i])
        

        def isUniversal(word):
            tempCounter = [0] * 26
            for char in word:
                tempCounter[ord(char)-ord("a")] += 1
            for i in range(26):
                if tempCounter[i] < counter[i]:
                    return False

            return True

        universals = []
        for word in words1:
            if isUniversal(word):
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
