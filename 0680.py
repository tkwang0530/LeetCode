"""
680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example1:
Input: s = "aba"
Output: true

Example2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space
"""




import unittest
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


# Unit Tests
funcs = [Solution().validPalindrome]


class TestValidPalindrome(unittest.TestCase):
    def testValidPalindrome1(self):
        for func in funcs:
            self.assertEqual(func(s="aba"), True)

    def testValidPalindrome2(self):
        for func in funcs:
            self.assertEqual(func(s="abca"), True)

    def testValidPalindrome3(self):
        for func in funcs:
            self.assertEqual(func(s="abc"), False)

if __name__ == "__main__":
    unittest.main()
