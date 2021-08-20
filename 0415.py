"""
415. Add Strings
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
1 <= num1.length, num2.length <= 10^4
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""

"""
Note:
1. Two Pointers: O(max(num1, num2)) time | O(1) space
"""




import unittest
class Solution(object):
    def addStrings(self, num1: str, num2: str) -> str:
        idx1 = len(num1) - 1
        idx2 = len(num2) - 1
        carry = 0
        result = []
        while idx1 >= 0 or idx2 >= 0 or carry > 0:
            value1 = self.charToNum(num1[idx1]) if idx1 >= 0 else 0
            value2 = self.charToNum(num2[idx2]) if idx2 >= 0 else 0
            total = value1 + value2 + carry
            carry = total // 10
            digit = total % 10
            result.append(str(digit))
            idx1 -= 1
            idx2 -= 1
        return "".join(result[::-1])


    def charToNum(self, char: str) -> int:
        return ord(char) - ord("0")

# Unit Tests

funcs = [Solution().addStrings]

class TestAddStrings(unittest.TestCase):
    def testAddStrings1(self):
        for func in funcs:
            num1 = "11"
            num2 = "123"
            self.assertEqual(func(num1=num1, num2=num2), "134")

    def testAddStrings2(self):
        for func in funcs:
            num1 = "456"
            num2 = "77"
            self.assertEqual(func(num1=num1, num2=num2), "533")

    def testAddStrings3(self):
        for func in funcs:
            num1 = "0"
            num2 = "0"
            self.assertEqual(func(num1=num1, num2=num2), "0")


if __name__ == "__main__":
    unittest.main()
