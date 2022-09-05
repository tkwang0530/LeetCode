"""
405. Convert a Number to Hexadecimal
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two's complement method is used.
(symbols "0"–"9" to represent values 0 to 9, and "A"–"F" (or alternatively "a"–"f") to represent values from 10 to 15.)

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

Example1:
Input: num = 26
Output: "1a"

Example2:
Input: num = -1
Output: "ffffffff"

Constraints:
-2^31 <= num <= 2^31 - 1
"""

"""
Note:
1. Brute-Force: O(1) time | O(1) space
To compute the two's complement of a n-digit hexadecimal numeral, either:
(1) complement each digit (exchange 0 for F, 1 for E, and so on) and then add one to the whole numeral
- complement the first digit using the appropriate number of bits. For example, with 22 bits, the first hexadecimal digit uses only two bits, so exchange 0 for 3, 1 for 2, 2 for 1, and 3 for 0.
(2) subtract the numeral from (In hexadecimal) one  followed by n zeroes.
- subtract from the appropriate power of two. For example, for 22 bits, subtract from (hexadecimal) 400000.
"""




import unittest
class Solution:
    def toHex(self, num: int) -> str:
        isNegative = num < 0
        num = abs(num)
        chars = ["0"] * 8

        numChar = {i: str(i) for i in range(0, 9+1)}
        charNum = {}
        for i in range(10, 16):
            numChar[i] = chr(ord('a')+i-10)

        for digit, char in numChar.items():
            charNum[char] = digit

        mod = 16
        i = len(chars) - 1
        while num > 0:
            r = num % mod
            num = num // mod
            chars[i] = numChar[r]
            i -= 1

        if isNegative:
            for i in range(len(chars)):
                chars[i] = numChar[(15-charNum[chars[i]])]
            carry = 1
            for i in range(len(chars)-1, -1, -1):
                charVal = charNum[chars[i]] + carry
                carry = charVal // 16
                chars[i] = numChar[charVal % 16]
                if carry == 0:
                    break

        start = 0
        while start < len(chars)-1 and chars[start] == "0":
            start += 1
        return "".join(chars[start:])


# Unit Tests
funcs = [Solution().toHex]


class TestToHex(unittest.TestCase):
    def testToHex1(self):
        for func in funcs:
            num = 26
            self.assertEqual(func(num=num), "1a")

    def testToHex2(self):
        for func in funcs:
            num = -1
            self.assertEqual(func(num=num), "ffffffff")


if __name__ == "__main__":
    unittest.main()
