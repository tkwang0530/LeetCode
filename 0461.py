"""
461. Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Example1:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example2:
Input: x = 3, y = 1
Output: 1

Constraints:
0 <= x, y <= 2^31 - 1
"""

"""
Note:
1. bin + zfill: O(32) time | O(64) space
"""




import unittest
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xbit, ybit = bin(x)[2:].zfill(32), bin(y)[2:].zfill(32)
        n = len(xbit)
        count = 0
        for i in range(n):
            count += xbit[i] != ybit[i]
        return count


# Unit Tests
funcs = [Solution().hammingDistance]


class TestHammingDistance(unittest.TestCase):
    def testHammingDistance1(self):
        for func in funcs:
            x = 1
            y = 4
            self.assertEqual(func(x=x, y=y), 2)

    def testHammingDistance2(self):
        for func in funcs:
            x = 3
            y = 1
            self.assertEqual(func(x=x, y=y), 1)


if __name__ == "__main__":
    unittest.main()
