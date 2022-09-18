"""
520. Detect Capital
We define the usage of capitals in a word to be right when one of the following cases holds:
- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.

Example1:
Input: word = "USA"
Output: true

Example2:
Input: word = "FlaG"
Output: false

Constraints:
1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""

"""
Note:
1. Brute Force: O(1) time | O(1) space
"""




import unittest
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.lower() or word == word.upper() or word == word[0].upper() + word[1:].lower()


# Unit Tests
funcs = [Solution().detectCapitalUse]


class TestDetectCapitalUse(unittest.TestCase):
    def testDetectCapitalUse1(self):
        for func in funcs:
            word = "USA"
            self.assertEqual(func(word=word), True)

    def testDetectCapitalUse2(self):
        for func in funcs:
            word = "FlaG"
            self.assertEqual(func(word=word), False)


if __name__ == "__main__":
    unittest.main()
