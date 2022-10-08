"""
2429. Given two positive integers num1 and num2, find the integer x such that:
- x has the same number of set bits as num2, and
- The value x XOR num1 is minimal.

Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the nubmer of 1's in its binary representation.

Example1:
Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.

Example2:
Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.

Constraints:
1 <= num1, num2 <= 10^9
"""

"""
Note:
1. Brute-Force: O(1) time | O(1) space
"""




import unittest
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        oneCount = bin(num2)[2:].count("1")
        binary = bin(num1)[2:].zfill(32)

        output = []
        for b in binary:
            if oneCount > 0 and b == '1':
                oneCount -= 1
                output.append("1")
            else:
                output.append("0")

        i = len(output) - 1
        while i >= 0 and oneCount > 0:
            if output[i] == '0':
                output[i] = '1'
                oneCount -= 1
            i -= 1
        return int(''.join(output), 2)


# Unit Tests
funcs = [Solution().minimizeXor]


class TestMinimizeXor(unittest.TestCase):
    def testMinimizeXor1(self):
        for func in funcs:
            num1 = 3
            num2 = 5
            self.assertEqual(func(num1=num1, num2=num2), 3)

    def testMinimizeXor2(self):
        for func in funcs:
            num1 = 1
            num2 = 12
            self.assertEqual(func(num1=num1, num2=num2), 3)


if __name__ == "__main__":
    unittest.main()
