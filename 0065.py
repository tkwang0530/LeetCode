"""
65. Valid Number
A valid number can be split up into these components (in order):
1. A decimal number or an integer.
2. (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-').
2. One of the following formats:
    1. One or more digits, followed by a dot '.' .
    2. One or more digits, followed by a dot '.' , followed by one or more digits.
    3. A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-')
2. One or more digits.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example1:
Input: s = "0"
Output: true

Example2:
Input: s = "e"
Output: false

Example3:
Input: s = ".1"
Output: true

Constraints:
1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.' .

"""

"""
Note:
1. one pass + 5 conditions check: O(n) time | O(1) space
3 boolean variables: hasSeenDigit, hasSeenEe, hasSeenDot
(1) "digit": update hasSeenDigit to True
(2) "+" or "-": if it doesn't at the index 0 and the char befor it isn't e or E: return False
(3) "e" or "E": if hasSeenEe or not hasSeenDigit, return False, otherwise update hasSeenDigit = False, hasSeenEe = True
(4) ".": if hasSeenEe or hasSeenDot: return False, otherwise update hasSeenDot to True
(5) other character: return False
Finally return hasSeenDigit
"""




import unittest
class Solution(object):
    def isNumber(self, s: str) -> bool:
        hasSeenDigit = hasSeenDot = hasSeenEe = False
        for i, char in enumerate(s):
            if char.isdigit():
                hasSeenDigit = True
            elif char in ("+", "-"):
                if i > 0 and s[i-1] not in ("E", "e"):
                    return False
            elif char in ("e", "E"):
                if hasSeenEe or not hasSeenDigit:
                    return False
                hasSeenEe = True
                hasSeenDigit = False
            elif char == ".":
                if hasSeenEe or hasSeenDot:
                    return False
                hasSeenDot = True
            else:
                return False
        return hasSeenDigit



# Unit Tests
funcs = [Solution().isNumber]


class TestIsNumber(unittest.TestCase):
    def testIsNumber1(self):
        for func in funcs:
            s = "0"
            self.assertEqual(func(s=s), True)

    def testIsNumber2(self):
        for func in funcs:
            s = "e"
            self.assertEqual(func(s=s), False)

    def testIsNumber3(self):
        for func in funcs:
            s = "."
            self.assertEqual(func(s=s), False)

    def testIsNumber4(self):
        for func in funcs:
            s = ".1"
            self.assertEqual(func(s=s), True)

    def testIsNumber5(self):
        for func in funcs:
            s = "-+3"
            self.assertEqual(func(s=s), False)

    def testIsNumber6(self):
        for func in funcs:
            s = "-123.456e789"
            self.assertEqual(func(s=s), True)

    def testIsNumber7(self):
        for func in funcs:
            s = "+6e-1"
            self.assertEqual(func(s=s), True)

    def testIsNumber8(self):
        for func in funcs:
            s = "0089"
            self.assertEqual(func(s=s), True)

    def testIsNumber9(self):
        for func in funcs:
            s = "95a54e53"
            self.assertEqual(func(s=s), False)

if __name__ == "__main__":
    unittest.main()
