"""
389. Find the Difference
You are given two strings s and t.
String t is generated by random shuffling string s and then add one more letter at a random position.
Return the letter that was added to t.

Example1:
Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example2:
Input: s = "", t = "y"
Output: "y"

Example3:
Input: s = "a", t = "aa"
Output: "a"

Example4:
Input: s = "ae", t = "aea"
Output: "a"

Constraints:
0 <= s.length <= 1000
t.length == s.length + 1
s and t consist of lower-case English letters.
"""

"""
Note:
1. Hash Table: O(n) time | O(1) space
2. Bit Manipulation xor (^): O(n) time | O(1) space
"""
import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        charCount = collections.Counter(s)
        for char in t:
            if char not in charCount or charCount[char] == 0:
                return char
            else:
                charCount[char] -= 1

    def findTheDifference2(self, s: str, t: str) -> str:
        result = 0
        for char in s+t:
            result ^= ord(char)
        return chr(result)

# Unit Tests
import unittest
funcs = [Solution().findTheDifference, Solution().findTheDifference2]


class TestFindTheDifference(unittest.TestCase):
    def testFindTheDifference1(self):
        for func in funcs:
            s = "abcd"
            t = "abcde"
            self.assertEqual(func(s=s, t=t), "e")

    def testFindTheDifference2(self):
        for func in funcs:
            s = ""
            t = "y"
            self.assertEqual(func(s=s, t=t), "y")

    def testFindTheDifference3(self):
        for func in funcs:
            s = "a"
            t = "aa"
            self.assertEqual(func(s=s, t=t), "a")

    def testFindTheDifference4(self):
        for func in funcs:
            s = "ae"
            t = "aea"
            self.assertEqual(func(s=s, t=t), "a")

if __name__ == "__main__":
    unittest.main()
