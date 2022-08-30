"""
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

""" 
Note:
1. HashTable: O(n) time | O(52) space
"""
import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCount = collections.Counter(s)
        hasOdd = False
        total = 0
        for count in charCount.values():
            if count >= 2:
                temp = count - 1 if count % 2 == 1 else count
                total += temp
                count -= temp
            if count > 0:
                hasOdd = True
            
        return total+1 if hasOdd else total

# Unit Tests
import unittest
funcs = [Solution().longestPalindrome]

class TestLongestPalindrome(unittest.TestCase):
    def testLongestPalindrome1(self):
        for func in funcs:
            self.assertEqual(func(s = "abccccdd"), 7)

    def testLongestPalindrome2(self):
        for func in funcs:
            self.assertEqual(func(s = "a"), 1)

if __name__ == "__main__":
    unittest.main()
