"""
500. Keyboard Row
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:
- the first row consists of characters "qwertyuiop",
- the second row consists of the characters "asdfghjkl", and
- the third row consists of the characters "zxcvbnm".

Example1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example2:
Input: words = ["omk"]
Output: []

Example3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

Constraints:
1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase).
"""

"""
Note:
1. HashTable: O(n * w) time | O(n) space - where n is the length of words and w is the average length of words
"""




from typing import List
import unittest
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRowSet = set(list("qwertyuiop"))
        secondRowSet = set(list("asdfghjkl"))
        thirdRowSet = set(list("zxcvbnm"))

        output = []
        for word in words:
            first = second = third = False
            for char in word.lower():
                if char in firstRowSet:
                    first = True
                if char in secondRowSet:
                    second = True
                if char in thirdRowSet:
                    third = True
            if first+second+third == 1:
                output.append(word)
        return output


# Unit Tests
funcs = [Solution().findWords]


class TestFindWords(unittest.TestCase):
    def testFindWords1(self):
        for func in funcs:
            words = ["Hello", "Alaska", "Dad", "Peace"]
            self.assertEqual(func(words=words), ["Alaska", "Dad"])

    def testFindWords2(self):
        for func in funcs:
            words = ["omk"]
            self.assertEqual(func(words=words), [])

    def testFindWords3(self):
        for func in funcs:
            words = ["adsdf", "sfd"]
            self.assertEqual(func(words=words), ["adsdf", "sfd"])


if __name__ == "__main__":
    unittest.main()
