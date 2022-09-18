"""
507. Perfect Number
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

Example1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example2:
Input: num = 7
Output: false

Constraints:
1 <= num <= 10^8
"""

"""
Note:
1. Brute Force: O(sqrt(num)) time | O(1) space
"""




import unittest
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return 0

        count = 1
        for i in range(2, int(num**0.5)+1):
            if i*i == num:
                count += num
            elif num % i == 0:
                count += i + num // i
        return num == count


# Unit Tests
funcs = [Solution().checkPerfectNumber]


class TestCheckPerfectNumber(unittest.TestCase):
    def testCheckPerfectNumber1(self):
        for func in funcs:
            num = 28
            self.assertEqual(func(num=num), True)

    def testCheckPerfectNumber2(self):
        for func in funcs:
            num = 7
            self.assertEqual(func(num=num), False)


if __name__ == "__main__":
    unittest.main()
