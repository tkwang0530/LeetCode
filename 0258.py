"""
258. Add Digits
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example2:
Input: num = 0
Output: 0

Constraints:
0 <= num <= 2^31 - 1
"""

"""
Note:
1. Brute-Force: O(1) time | O(1) space
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum([int(char) for char in str(num)])
        return num

# Unit Tests
import unittest
funcs = [Solution().addDigits]
class TestAddDigits(unittest.TestCase):
    def testAddDigits1(self):
        for func in funcs:
            self.assertEqual(func(num = 38), 2)

    def testAddDigits2(self):
        for func in funcs:
            self.assertEqual(func(num = 0), 0)

if __name__ == "__main__":
    unittest.main()
