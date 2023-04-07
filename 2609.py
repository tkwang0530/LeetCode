"""
2609. Find the Longest Balanced Substring of a Binary String
You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

Return the length of the longest balanced substring of s.

A substring is a contiguous sequence of characters within a string.

Example1:
Input: s = "01000111"
Output: 6
Explanation: The longest balanced substring is "000111", which has length 6.

Example2:
Input: s = "00111"
Output: 4
Explanation: The longest balanced substring is "0011", which has length 4. 

Example3:
Input: s = "111"
Output: 0
Explanation: There is no balanced substring except the empty substring, so the answer is 0.

Constraints:
1 <= s.length <= 50
'0' <= s[i] <= '1'
"""

"""
Note:
1. Brute-Force: O(n) time | O(1) space - where n is the length of string s
"""




import unittest
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeroCount = 0
        oneCount = 0
        maxLength = 0
        for char in s:
            if char == "0":
                if oneCount > 0:
                    zeroCount = 0
                zeroCount += 1
                oneCount = 0
            else:
                oneCount += 1
                maxLength = max(maxLength, min(oneCount, zeroCount)*2)
        return maxLength


# Unit Tests
funcs = [Solution().findTheLongestBalancedSubstring]


class TestFindTheLongestBalancedSubstring(unittest.TestCase):
    def testFindTheLongestBalancedSubstring1(self):
        for func in funcs:
            s = "01000111"
            self.assertEqual(func(s=s), 6)

    def testFindTheLongestBalancedSubstring2(self):
        for func in funcs:
            s = "00111"
            self.assertEqual(func(s=s), 4)

    def testFindTheLongestBalancedSubstring3(self):
        for func in funcs:
            s = "111"
            self.assertEqual(func(s=s), 0)


if __name__ == "__main__":
    unittest.main()
