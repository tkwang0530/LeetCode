"""
371. Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the operators + and - .

Example1:
Input: a = 1, b = 2
Output: 3

Example2:
Input: a = 2, b = 3
Output: 5

Constraints:
-1000 <= a, b <= 1000
"""

"""
Note:
1. Bit Manipulation: O(1) time | O(1) space
Use ^ to find the digit
Use & to find the carry
"""

class Solution(object):
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # mask to get last 32 bits
        mask = 0xFFFFFFFF

        while b != 0:
            # ^ get different bits and and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative 
        # (e.g. -2-> 10000....1, 1-> 00000....1)
        return a if a <= MAX else ~(a ^ mask)


# Unit Tests
import unittest
funcs = [Solution().getSum]

class TestGetSum(unittest.TestCase):
    def testGetSum1(self):
        for func in funcs:
            a = 1
            b = 2
            self.assertEqual(func(a=a, b=b), 3)

    def testGetSum2(self):
        for func in funcs:
            a = 2
            b = 3
            self.assertEqual(func(a=a, b=b), 5)

    def testGetSum3(self):
        for func in funcs:
            a = -2
            b = 3
            self.assertEqual(func(a=a, b=b), 1)

    def testGetSum4(self):
        for func in funcs:
            a = -2
            b = -3
            self.assertEqual(func(a=a, b=b), -5)

if __name__ == "__main__":
    unittest.main()
