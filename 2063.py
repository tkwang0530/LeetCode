"""
2063. Vowels of All Substrings
Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring of word.

A substring is a contiguous (non-empty) sequence of characters within a string.

Note: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.

Example1:
Input: word = "aba"
Output: 6
Explanation: 
All possible substrings are: "a", "ab", "aba", "b", "ba", and "a".
- "b" has 0 vowels in it
- "a", "ab", "ba", and "a" have 1 vowel each
- "aba" has 2 vowels in it
Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6. 

Example2:
Input: word = "abc"
Output: 3
Explanation: 
All possible substrings are: "a", "ab", "abc", "b", "bc", and "c".
- "a", "ab", and "abc" have 1 vowel each
- "b", "bc", and "c" have 0 vowels each
Hence, the total sum of vowels = 1 + 1 + 1 + 0 + 0 + 0 = 3.

Example3:
Input: word = "ltcd"
Output: 0
Explanation: There are no vowels in any substring of "ltcd".

Constraints:
1 <= word.length <= 10^5
word consists of lowercase English letters.
"""

"""
Note:
1. Math: O(n) time | O(1) space
For each vowels s[i],
it could be in the substring string at s[x] and ending at s[y].
where 0 <= x <= i and i <= y < n.
that is (i+1) choices for x and (n-i) choices for y.
so there are (i+1)*(n-i) substrings containing s[i].
"""

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        result = 0
        for i in range(n):
            if word[i] in "aeiou":
                result += (i+1) * (n-i)
        return result

# Unit Tests
import unittest
funcs = [Solution().countVowels]

class TestCountVowels(unittest.TestCase):
    def testCountVowels1(self):
        for func in funcs:
            word = "aba"
            self.assertEqual(func(word=word), 6)

    def testCountVowels2(self):
        for func in funcs:
            word = "abc"
            self.assertEqual(func(word=word), 3)

    def testCountVowels3(self):
        for func in funcs:
            word = "ltcd"
            self.assertEqual(func(word=word), 0)

if __name__ == "__main__":
    unittest.main()