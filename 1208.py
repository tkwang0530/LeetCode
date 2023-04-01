"""
1208. Get Equal Substrings Within Budget
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of  a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example1:
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.

Example2:
Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.

Example3:
Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.

Constraints:
1 <= s.length <= 10^5
t.length == s.length
0 <= maxCost <= 10^6
s and t consist of only lowercase English letters.
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space - where n is the length of string s
"""




import unittest
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        maxLen = 0
        currentCost = 0
        start = 0
        for end in range(n):
            sChar, tChar = s[end], t[end]
            currentCost += abs(ord(sChar) - ord(tChar))
            while currentCost > maxCost:
                sLeftChar, tLeftChar = s[start], t[start]
                currentCost -= abs(ord(sLeftChar) - ord(tLeftChar))
                start += 1
            maxLen = max(maxLen, end - start + 1)
        return maxLen


# Unit Tests
funcs = [Solution().equalSubstring]


class TestEqualSubstring(unittest.TestCase):
    def testEqualSubstring1(self):
        for func in funcs:
            s = "abcd"
            t = "bcdf"
            maxCost = 3
            self.assertEqual(func(s=s, t=t, maxCost=maxCost), 3)

    def testEqualSubstring2(self):
        for func in funcs:
            s = "abcd"
            t = "cdef"
            maxCost = 3
            self.assertEqual(func(s=s, t=t, maxCost=maxCost), 1)

    def testEqualSubstring3(self):
        for func in funcs:
            s = "abcd"
            t = "acde"
            maxCost = 0
            self.assertEqual(func(s=s, t=t, maxCost=maxCost), 1)


if __name__ == "__main__":
    unittest.main()
