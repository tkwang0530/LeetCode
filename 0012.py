"""
12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is Written as XII, which is simply X + II. The number 27 is written as XXVII.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used.
- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C(100) to make 40 and 90.
- C can be placed before D (500) and M(1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Examples:
    Given 3, the answer is "III".
    Given 4, the answer is "IV".
    Given 9, the answer is "IX".
    Given 58, the answer is "LVIII".
    Given 1994, the answer is "MCMXCIV".

Constraints:
1 <= num <= 3999
"""

# O(1) time | O(1) space
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]
        ans = []
        for i, value in enumerate(values):
            ans.append(num // value * numerals[i])
            num %= value
        return "".join(ans)


# Unit Tests
import unittest


class TestIntToRoman(unittest.TestCase):
    def testIntToRoman1(self):
        func = Solution().intToRoman
        self.assertEqual(func(num=3), "III")

    def testIntToRoman2(self):
        func = Solution().intToRoman
        self.assertEqual(func(num=4), "IV")

    def testIntToRoman3(self):
        func = Solution().intToRoman
        self.assertEqual(func(num=9), "IX")

    def testIntToRoman4(self):
        func = Solution().intToRoman
        self.assertEqual(func(num=58), "LVIII")

    def testIntToRoman5(self):
        func = Solution().intToRoman
        self.assertEqual(func(num=1994), "MCMXCIV")


if __name__ == "__main__":
    unittest.main()