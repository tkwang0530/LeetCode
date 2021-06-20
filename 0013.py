"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is Written as XII, which is simply X + II. The number 27 is written as XXVII.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used.
- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C(100) to make 40 and 90.
- C can be placed before D (500) and M(1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Examples:
    Given "III", the answer is 3.
    Given "IV",  the answer is 4.
    Given "IX", the answer is 9.
    Given "LVIII", the answer is 58.
    Given "MCMXCIV", the answer is 1994.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'D', 'M').
It is guaranteed that s is a valid roman numeral in range [1, 3999].
"""

"""
Note:
O(15) time | O(1) space
The trick is that the last letter is always added. Except the last one, if one letter is less than its latter one, this letter is subtracted.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        z = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]


# Unit Tests
import unittest


class TestRomanToInt(unittest.TestCase):
    def testRomanToInt1(self):
        func = Solution().romanToInt
        self.assertEqual(func(s="III"), 3)

    def testRomanToInt2(self):
        func = Solution().romanToInt
        self.assertEqual(func(s="IV"), 4)

    def testRomanToInt3(self):
        func = Solution().romanToInt
        self.assertEqual(func(s="IX"), 9)

    def testRomanToInt4(self):
        func = Solution().romanToInt
        self.assertEqual(func(s="LVIII"), 58)

    def testRomanToInt5(self):
        func = Solution().romanToInt
        self.assertEqual(func(s="MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()