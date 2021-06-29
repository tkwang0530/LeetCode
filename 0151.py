"""
151. Reverse Words in a String
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Example4:
Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"

Example5:
Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"

Constraints:
1 <= s.length <= 10^4
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow up: if the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""

"""
Note:
1. split() + reverse: O(n) time | O(n) space
2. Two Pointers: O(n) time | O(n) space
traverse + manual add space + skip space
"""




from typing import List
import unittest
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

    def reverseWords2(self, s: str) -> str:
        words = []
        left, right = 0, len(s) - 1
        while left < len(s) and s[left] == " ":
            left += 1
        startOfWord = left
        while right >= 0 and s[right] == " ":
            right -= 1

        while left <= right:
            char = s[left]
            if char == " ":
                words.append(s[startOfWord:left])
                while left <= right and s[left] == " ":
                    left += 1
                startOfWord = left
            left += 1
        words.append(s[startOfWord:right+1])
        self.reverseList(words)
        return " ".join(words)

    def reverseList(self, list: List[str]):
        left, right = 0, len(list) - 1
        while left < right:
            list[left], list[right] = list[right], list[left]
            left, right = left + 1, right - 1


# Unit Tests
funcs = [Solution().reverseWords, Solution().reverseWords2]


class TestReverseWords(unittest.TestCase):
    def testReverseWords1(self):
        for func in funcs:
            self.assertEqual(func(s="the sky is blue"), "blue is sky the")

    def testReverseWords2(self):
        for func in funcs:
            self.assertEqual(func(s="  hello world  "), "world hello")

    def testReverseWords3(self):
        for func in funcs:
            self.assertEqual(func(s="a good   example"), "example good a")

    def testReverseWords4(self):
        for func in funcs:
            self.assertEqual(
                func(s="  Bob    Loves  Alice   "), "Alice Loves Bob")

    def testReverseWords5(self):
        for func in funcs:
            self.assertEqual(
                func(s="Alice does not even like bob"), "bob like even not does Alice")


if __name__ == "__main__":
    unittest.main()
