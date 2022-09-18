"""
476. Number Complement
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
- For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.

Given an integer num, return its complement.

Example1:
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example2:
Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


Constraints:
1 <= num < 2^31
"""

"""
Note:
1. Brute-Force: O(1) time | O(1) space
"""




import unittest
class Solution:
    def findComplement(self, num: int) -> int:
        binaryStr = bin(num)[2:]
        complement = 0
        power = 0
        for i in range(len(binaryStr)-1, -1, -1):
            b = binaryStr[i]
            complement += 2**power if not int(b) else 0
            power += 1
        return complement


# Unit Tests
funcs = [Solution().findComplement]


class TestFindComplement(unittest.TestCase):
    def testFindComplement1(self):
        for func in funcs:
            num = 5
            self.assertEqual(func(num=num), 2)

    def testFindComplement2(self):
        for func in funcs:
            num = 1
            self.assertEqual(func(num=num), 0)


if __name__ == "__main__":
    unittest.main()
