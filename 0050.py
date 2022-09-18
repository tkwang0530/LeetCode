"""
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n)

Example1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

"""
Notes:
1. Recursion (Divide and conquer): O(logn) time | O(logn) space
(1) concept
2^10 = 2^5 * 2^5
2^5 = 2 * 2^2 * 2^2
2^2 = 2 * 2
(2) base case
x = 0, return 0
n = 0, return 1
"""




import unittest
class Solution(object):
    def myPow(self, x: float, n: int) -> float:
        def pow(x: float, n: int) -> float:
            if x == 0:
                return 0
            if n == 0:
                return 1

            result = pow(x*x, n//2)
            return x * result if n % 2 else result
        result = pow(x, abs(n))
        return result if n >= 0 else 1/result


# Unit Tests
funcs = [Solution().myPow]


class TestMyPow(unittest.TestCase):
    def testMyPow1(self):
        for func in funcs:
            x = 2.00000
            n = 10
            self.assertTrue(abs(func(x, n) - 1024) < 1/(10**10))

    def testMyPow2(self):
        for func in funcs:
            x = 2.10000
            n = 3
            self.assertTrue(abs(func(x, n)-9.26100) < 1/(10**10))

    def testMyPow3(self):
        for func in funcs:
            x = 2.00000
            n = -2
            self.assertTrue(abs(func(x, n)-0.25) < 1/(10**10))


if __name__ == "__main__":
    unittest.main()
