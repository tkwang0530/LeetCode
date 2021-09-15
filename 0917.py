"""
917. Reverse Only Letters
Given a string s, reverse the string according to the following rules:
- All the characters that are not English letters remain in the same position.
- All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

Example1:
Input: s = "ab-cd"
Output: "dc-ba"

Example2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\' .
"""

"""
Notes:
1. store letters to a list: O(n) time | O(n) space
2. Two Pointers: O(n) time | O(n) space
(1) use isalpha()
(2) if isalpha() exchange char in left and in right, otherwise skip it
(3) return "".join(chars)
"""
class Solution(object):
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [char for char in s if char.isalpha()]
        
        j = len(letters) - 1
        result = []
        for i in range(len(s)):
            if s[i].isalpha():
                result.append(letters[j])
                j -= 1
            else:
                result.append(s[i])
        return "".join(result)

    def reverseOnlyLetters2(self, s: str) -> str:
        chars = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not chars[left].isalpha():
                left += 1
            while left < right and not chars[right].isalpha():
                right -= 1
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return "".join(chars)

# Unit Tests
import unittest
funcs = [Solution().reverseOnlyLetters, Solution().reverseOnlyLetters2]

class TestReverseOnlyLetters(unittest.TestCase):
    def testReverseOnlyLetters1(self):
        for func in funcs:
            self.assertEqual(func(s="ab-cd"), "dc-ba")

    def testReverseOnlyLetters2(self):
        for func in funcs:
            self.assertEqual(func(s="a-bC-dEf-ghIj"), "j-Ih-gfE-dCba")

    def testReverseOnlyLetters3(self):
        for func in funcs:
            self.assertEqual(func(s="Test1ng-Leet=code-Q!"), "Qedo1ct-eeLg=ntse-T!")


if __name__ == "__main__":
    unittest.main()