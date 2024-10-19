"""
1545. Find Kth Bit in Nth Binary String
description: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description 
"""

"""
Note:
1. bitwise operation: O(2^n) time | O(2^n) space
"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        bits = [0]
        for _ in range(n-1):
            bits.append(1)
            bits.extend([b ^ 1 for b in bits[:-1][::-1]])
        return str(bits[k-1])

funcs = [Solution().findKthBit]

import unittest
class TestFindKthBit(unittest.TestCase):
    def testFindKthBit1(self):
        for func in funcs:
            n = 3
            k = 1
            self.assertEqual(func(n=n, k=k), "0")

    def testFindKthBit2(self):
        for func in funcs:
            n = 4
            k = 11
            self.assertEqual(func(n=n, k=k), "1")

if __name__ == "__main__":
    unittest.main()
