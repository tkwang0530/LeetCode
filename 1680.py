"""
1680. Concatenation of Consecutive Binary Numbers
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 10^9 + 7.

Example1:
Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 

Example2:
Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

Example3:
Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.

Constraints:
1 <= n <= 10^5
"""

""" 
1. Bit manipulation: O(n) time | O(1) space
"""

import math
class Solution(object):
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        current = prev = 0
        for i in range(1, n+1):
            current = (prev << int(math.log2(i))+1) + i
            current %= MOD
            prev = current
        return prev

# Unit Tests
import unittest
funcs = [Solution().concatenatedBinary]


class TestConcatenatedBinary(unittest.TestCase):
    def testConcatenatedBinary1(self):
        for func in funcs:
            n = 1
            self.assertEqual(func(n=n), 1)

    def testConcatenatedBinary2(self):
        for func in funcs:
            n = 3
            self.assertEqual(func(n=n), 27)

    def testConcatenatedBinary3(self):
        for func in funcs:
            n = 12
            self.assertEqual(func(n=n), 505379714)

if __name__ == "__main__":
    unittest.main()
