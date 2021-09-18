"""
191. Number of 1 Bits
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
Note:
- Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

Example1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:
The input must be a binary string of length 32

Follow up: If this function is called many times, how would you optimize it?
"""
"""
Notes:
1. Bit Manipulation: O(1) time | O(1) space
2. Built-in function bin and count: O(1) time | O(1) space
bin(a)
Parameters: a is an integer to convert
Return value: A binary string of an integer or int object
Exceptions: Raises TypeError when a float value if sent in arguments.
The result will always start with the prefix 0b.

3. Bit Manipulation (optimize): O(1) time | O(1) space
n & n-1 will remove the rightmost in binary representation of n
For example,
n              = 10110100
n-1           = 10110011
n&(n-1)   = 10110000
What we need to do now, just repeat this operation until we have n = 0 and count number of steps
"""

class Solution(object):
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if (1 << i) & n > 0:
                count += 1
        return count
    
    def hammingWeight2(self, n: int) -> int:
        return bin(n).count("1")

    def hammingWeight3(self, n: int) -> int:
        count = 0
        while n > 0:
            n &= (n-1)
            count += 1
        return count

# Unit Tests
import unittest
funcs = [Solution().hammingWeight, Solution().hammingWeight2, Solution().hammingWeight3]

class TestHammingWeight(unittest.TestCase):
    def testHammingWeight1(self):
        for func in funcs:
            self.assertEqual(func(n=11), 3)

    def testHammingWeight2(self):
        for func in funcs:
            self.assertEqual(func(n=2**7), 1)

    def testHammingWeight3(self):
        for func in funcs:
            self.assertEqual(func(n=2**32-3), 31)


if __name__ == "__main__":
    unittest.main()