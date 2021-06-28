"""
125. Valid Palindrome
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters
"""

"""
Note:
1. Two pointers: O(n) time | O(1) space
"""




import unittest
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# Unit Tests
funcs = [Solution().isPalindrome]


class TestIsPalindrome(unittest.TestCase):
    def testIsPalindrome1(self):
        for func in funcs:
            self.assertEqual(func(s="A man, a plan, a canal: Panama"), True)

    def testIsPalindrome2(self):
        for func in funcs:
            self.assertEqual(func(s="race a car"), False)


if __name__ == "__main__":
    unittest.main()
