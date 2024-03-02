"""
1737. Change Minimum Characters to Satisfy One of Three Conditions
description: https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/description/
"""

"""
Note:
1. PreSum + Counter: O(n+m) time | O(1) space - where n is the length of a and m is the length of b
"""

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        counterA = [0] * 26
        counterB = [0] * 26
        for char in a:
            counterA[ord(char) - ord("a")] += 1
        
        for char in b:
            counterB[ord(char) - ord("a")] += 1

        preSumA = [0] * 27
        preSumB = [0] * 27

        for i in range(1, 27):
            preSumA[i] = preSumA[i-1] + counterA[i-1]
            preSumB[i] = preSumB[i-1] + counterB[i-1]

        ans = max(len(a), len(b))
        for char in range(26):
            # i > 1
            # condition1: Every letter in a is strictly less than every letter in b in the alphabet.
            # set min(b) == char at i
            if char > 0:
                ans = min(ans, len(a) - preSumA[char] + preSumB[char])

            # condition2: Every letter in b is strictly less than every letter in a in the alphabet.
            # set min(a) == char at i
            if char > 0:
                ans = min(ans, len(b) - preSumB[char] + preSumA[char])

            # condition3: Both a and b consist of only one distinct letter.
            ans = min(ans, len(a)-counterA[char] + len(b)-counterB[char])

        return ans


# Unit Tests
import unittest
funcs = [Solution().minCharacters]
class TestMinCharacters(unittest.TestCase):
    def testMinCharacters1(self):
        for func in funcs:
            a = "aba"
            b = "caa"
            self.assertEqual(func(a=a, b=b), 2)

    def testMinCharacters2(self):
        for func in funcs:
            a = "dabadd"
            b = "cda"
            self.assertEqual(func(a=a, b=b), 3)

if __name__ == "__main__":
    unittest.main()
