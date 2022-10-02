"""
747. Shortest Completing Word
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, than it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

Example1:
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.

Example2:
Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.

Constraints:
1 <= licensePlate.length <= 7
licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
1 <= words.length <= 1000
1 <= words[i].length <= 15
words[i] consists of lower case English letters.
"""

"""
Note:
1. HashTables: O(n) time | O(1) space - where n is the length of array words
"""




import unittest
import collections
from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        standard = collections.defaultdict(int)
        for char in licensePlate:
            if char.isalpha():
                standard[char.lower()] += 1

        minLength = float("inf")
        candidate = ""
        for word in words:
            isValid = True
            wordCharCount = collections.Counter(word)
            for char, count in standard.items():
                if wordCharCount[char] < count:
                    isValid = False
                    break
            if isValid and len(word) < minLength:
                minLength = len(word)
                candidate = word
        return candidate


# Unit Tests
funcs = [Solution().shortestCompletingWord]


class TestShortestCompletingWord(unittest.TestCase):
    def testShortestCompletingWord1(self):
        for func in funcs:
            licensePlate = "1s3 PSt"
            words = ["step", "steps", "stripe", "stepple"]
            self.assertEqual(
                func(licensePlate=licensePlate, words=words), "steps")

    def testShortestCompletingWord2(self):
        for func in funcs:
            licensePlate = "1s3 456"
            words = ["looks", "pest", "stew", "show"]
            self.assertEqual(
                func(licensePlate=licensePlate, words=words), "pest")


if __name__ == "__main__":
    unittest.main()
