"""
953. Verifying an Alien Dictionary
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

"""
Note:
1. Using HashMap and zip: O(nxm) time | O(1) space
{alphabet: index}
before zip: ["word", "world", "row"]
after zip: [("word", "world"), ("world", "row")]

before zip: "word", "world"
after zip: [("w", "w"), ("o", "o"), ("r", "r"), ("d", "l") ...]
"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lookup = {}
        for idx, char in enumerate(order):
            lookup[char] = idx
        
        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return False
            for char1, char2 in zip(word1, word2):
                if lookup[char1] > lookup[char2]:
                    return False
                elif lookup[char1] < lookup[char2]:
                    break
        return True


# Unit Tests
import unittest
funcs = [Solution().isAlienSorted]

class TestIsAlienSorted(unittest.TestCase):
    def testIsAlienSorted1(self):
        for func in funcs:
            words = ["hello","leetcode"]
            order = "hlabcdefgijkmnopqrstuvwxyz"
            self.assertEqual(
                func(words=words, order=order), True
            )


    def testIsAlienSorted2(self):
        for func in funcs:
            words = ["word","world","row"]
            order = "worldabcefghijkmnpqstuvxyz"
            self.assertEqual(
                func(
                    words=words,
                    order=order
                ),
               False,
            )

    def testIsAlienSorted3(self):
        for func in funcs:
            words = ["apple","app"]
            order = "abcdefghijklmnopqrstuvwxyz"
            self.assertEqual(
                func(
                    words=words,
                    order=order
                ),
                False,
            )

if __name__ == "__main__":
    unittest.main()