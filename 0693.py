"""
693. Binary Number with Alternating Bits
Given a positive integer, check whether it has alternating bits; namely, if two adjacent bits will always have different values.

Example1:
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example2:
Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.

Example3:
Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.

Constraints:
1 <= n <= 2^31
"""

"""
Note:
1. Brute-Force: O(1) time | O(1) space
"""




import unittest
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = list(bin(n)[2:])
        prev = binary.pop()
        while binary:
            current = binary.pop()
            if current == prev:
                return False
            prev = current
        return True


# Unit Tests
funcs = [Solution().hasAlternatingBits]


class TestHasAlternatingBits(unittest.TestCase):
    def testHasAlternatingBits1(self):
        for func in funcs:
            self.assertEqual(func(n=5), True)

    def testHasAlternatingBits2(self):
        for func in funcs:
            self.assertEqual(func(n=7), False)

    def testHasAlternatingBits3(self):
        for func in funcs:
            self.assertEqual(func(n=11), False)


if __name__ == "__main__":
    unittest.main()
