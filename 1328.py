"""
1328. Break a Palindrome
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

Example1:
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example2:
Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

Constraints:
1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space - where n is the length of given string palindrome
"""




import unittest
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        left = 0
        right = len(palindrome) - 1
        chars = list(palindrome)
        while left <= right:
            if chars[left] == "a" or left == right:
                left += 1
                right -= 1
            elif left != right and chars[left]:
                chars[left] = "a"
                return "".join(chars)

        chars[-1] = "b"
        return "".join(chars)


# Unit Tests
funcs = [Solution().breakPalindrome]


class TestBreakPalindrome(unittest.TestCase):
    def testBreakPalindrome1(self):
        for func in funcs:
            palindrome = "abccba"
            self.assertEqual(func(palindrome=palindrome), "aaccba")

    def testBreakPalindrome2(self):
        for func in funcs:
            palindrome = "a"
            self.assertEqual(func(palindrome=palindrome), "")


if __name__ == "__main__":
    unittest.main()
