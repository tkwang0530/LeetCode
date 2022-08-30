"""
441. Arranging Coins
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the i-th row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:
1 <= n <= 2^31 - 1
"""

"""
Note:
1. Math: O(1) time | O(1) space
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # (1+x)*x = 2n => x^2 + x - 2n = 0 A=1 B=1 C=-2n
        def solve(n):
            return (-1+(1-4*1*(-2*n))**0.5)/ 2
        return int(solve(n))

# Unit Tests
import unittest
funcs = [Solution().arrangeCoins]

class TestArrangeCoins(unittest.TestCase):
    def testArrangeCoins1(self):
        for func in funcs:
            self.assertEqual(func(n = 5), 2)

    def testArrangeCoins2(self):
        for func in funcs:
            self.assertEqual(func(n = 8), 3)

if __name__ == "__main__":
    unittest.main()