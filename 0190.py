"""
190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

Note:
- Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Follow up: If this function is called many times, how would you optimize it?

Example1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

Constraints:
The input must be a binary string of length 32
"""
"""
Notes:
1. Bit Manipulation: O(1) time | O(1) space
01 << 1 = 10, & operation to retrieve bit,  | operation to put bit
"""

class Solution(object):
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31-i))
        return result

# Unit Tests
import unittest
funcs = [Solution().reverseBits]

class TestReverseBits(unittest.TestCase):
    def testReverseBits1(self):
        for func in funcs:
            self.assertEqual(func(n=43261596), 964176192)

    def testReverseBits2(self):
        for func in funcs:
            self.assertEqual(func(n=4294967293), 3221225471)


if __name__ == "__main__":
    unittest.main()