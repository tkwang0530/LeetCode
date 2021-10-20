"""
66. Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example3:
Input: digits = [0]
Output: [1]
Explanation: The array represents the integer 0.
Incrementing by one gives 0 + 1 = 1.
Thus, the result should be [1].

Example4:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""

"""
Note:
1. One Pass: O(n) time | O(1) space
"""

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        carry = 1
        while index >= 0:
            currentSum = digits[index] + carry
            carry = currentSum // 10
            remainder = currentSum % 10
            digits[index]  = remainder
            if carry:
                index -= 1
            else:
                return digits
        return [1] + digits


# Unit Tests
import unittest
funcs = [Solution().plusOne]

class TestPlusOne(unittest.TestCase):
    def testPlusOne1(self):
        for func in funcs:
            digits = [1,2,3]
            self.assertEqual(func(digits=digits), [1, 2, 4])

    def testPlusOne2(self):
        for func in funcs:
            digits = [4,3,2,1]
            self.assertEqual(func(digits=digits), [4,3,2,2])

    def testPlusOne3(self):
        for func in funcs:
            digits = [0]
            self.assertEqual(func(digits=digits), [1])

    def testPlusOne4(self):
        for func in funcs:
            digits = [9]
            self.assertEqual(func(digits=digits), [1,0])

if __name__ == "__main__":
    unittest.main()