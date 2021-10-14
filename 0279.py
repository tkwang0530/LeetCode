"""
279. Perfect Squares
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
1 <= n.length <= 10^4
"""

"""
Note:
1. Recursion + cache: O(n*sqrt(n)) time | O(n) space
"""

from typing import Dict
class Solution:
    def numSquares(self, n: int) -> int:
        cache = {0: 0, 1: 1}
        return self.numSquaresHelper(n, cache)
    
    def numSquaresHelper(self, n: int,  cache: Dict) -> int:
        if n in cache:
            return cache[n]
        maxPerfectNumber = int(n ** 0.5)
        minCount = float("inf")
        for i in range(maxPerfectNumber, 0, -1):
            minCount = min(minCount, 1 + self.numSquaresHelper(n - i * i, cache))
        cache[n] = minCount
        return cache[n]


# Unit Tests
import unittest
funcs = [Solution().numSquares]


class TestNumSquares(unittest.TestCase):
    def testNumSquares1(self):
        for func in funcs:
            self.assertEqual(func(n=12), 3)

    def testNumSquares2(self):
        for func in funcs:
            self.assertEqual(func(n=13), 2)

if __name__ == "__main__":
    unittest.main()
