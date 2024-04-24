"""
1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0
Given n , return the value of Tn

Example1:
Input: n = 4
Output: 4
"""

"""
Note:
1. Recursion: O(3^n) time | O(n) space

2. Iteration: O(n) time | O(1) space
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

class Solution2:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        n1, n2, n3 = 0, 1, 1
        for _ in range(n-2):
            n1, n2, n3 = n2, n3, n1+n2+n3
        return n3


# Unit Tests
import unittest


funcs = [Solution().tribonacci, Solution2().tribonacci]
class TestTribonacci(unittest.TestCase):
    def testTribonacci1(self):
        for func in funcs:
            n = 4
            self.assertEqual(func(n), 4)

    def testTribonacci2(self):
        for func in funcs:
            n = 25
            self.assertEqual(func(n), 1389537)


if __name__ == "__main__":
    unittest.main()