"""
345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example1:
Input: s = "hello"
Output: "holle"

Example2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.
"""

"""
Note:
1. Brute-Force: O(n) time | O(n) space - where n is the length of string s
"""




import unittest
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelIndice = []
        vowels = []
        vowelSet = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for i, char in enumerate(s):
            if char not in vowelSet:
                continue
            vowelIndice.append(i)
            vowels.append(char)

        vowels.reverse()
        chars = list(s)

        i = 0
        while i < len(vowels):
            idx = vowelIndice[i]
            vowel = vowels[i]
            chars[idx] = vowel
            i += 1
        return "".join(chars)


# Unit Tests
funcs = [Solution().reverseVowels]


class TestReverseVowels(unittest.TestCase):
    def testReverseVowels1(self):
        for func in funcs:
            s = "hello"
            self.assertEqual(func(s=s), "holle")

    def testReverseVowels2(self):
        for func in funcs:
            s = "leetcode"
            self.assertEqual(func(s=s), "leotcede")


if __name__ == "__main__":
    unittest.main()
