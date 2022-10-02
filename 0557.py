"""
557. Reverse Words in a String III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example2:
Input: s = "God Ding"
Output: "doG gniD"

Constraints:
1 <= s.length <= 5 * 10^4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""

"""
Note:
1. Brute-Force: O(n) time | O(n) space - where n is the length of string s
"""




import unittest
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        output = []
        for word in words:
            output.append(word[::-1])
        return " ".join(output)


# Unit Tests
funcs = [Solution().reverseWords]


class TestReverseWords(unittest.TestCase):
    def testReverseWords1(self):
        for func in funcs:
            s = "Let's take LeetCode contest"
            self.assertEqual(func(s=s), "s'teL ekat edoCteeL tsetnoc")

    def testReverseWords2(self):
        for func in funcs:
            s = "God Ding"
            self.assertEqual(func(s=s), "doG gniD")


if __name__ == "__main__":
    unittest.main()
