"""
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

""" 
1. Convert the number manually: O(n + m) time | O(1) space - where n is the length of num1 and m is the length of num2
But this sol may lead to stack overflow in same language
2. Perform multiplication on every pair of digits: O(n * m)  time | O(n + m) space - where n is the length of num1 and m is the length of num2
"""

class Solution(object):
    def multiply(self, num1: str, num2: str) -> str:
        list1 = list(num1)
        value1 = 0
        for i in range(len(list1)):
            value1 = value1 * 10 + (ord(list1[i]) - ord("0"))
        
        list2 = list(num2)
        value2 = 0
        for i in range(len(list2)):
            value2 = value2 * 10 + (ord(list2[i]) - ord("0"))
            
        return str(value1 * value2)

    def multiply2(self, num1: str, num2: str) -> str:
        digits = [0] * (len(num1) + len(num2))
        for i in range(len(num1) -1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                multiply = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                pos1, pos2 = i + j, i + j + 1
                sum = multiply + digits[pos2]
                digits[pos1] += sum // 10
                digits[pos2] = sum % 10
        counter = 0
        while counter < len(digits) - 1 and digits[counter] == 0:
            counter += 1
        return "".join(str(digit) for digit in digits[counter:])



# Unit Tests
import unittest
funcs = [Solution().multiply, Solution().multiply2]

class TestMultiply(unittest.TestCase):
    def testMultiply1(self):
        for func in funcs:
            num1 = "2"
            num2 = "3"
            self.assertEqual(func(num1=num1, num2=num2), "6")

    def testMultiply2(self):
        for func in funcs:
            num1 = "123"
            num2 = "456"
            self.assertEqual(func(num1=num1, num2=num2), "56088")

if __name__ == "__main__":
    unittest.main()
