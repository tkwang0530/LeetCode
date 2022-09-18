"""
738. 
An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y

Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

Example1:
Input: n = 10
Output: 9

Example2:
Input: n = 1234
Output: 1234

Example3:
Input: n = 332
Output: 299

Constraints:
0 <= n <= 10^9
"""

"""
Note:
1. Greedy: O(1) time | O(1) space
"""




import unittest
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        chars = list(str(n))
        L = len(chars)
        output = []
        for i in range(len(chars)):
            lowerBound = int("".join(output) + chars[i] * (L-i))
            if lowerBound <= n:
                output.append(chars[i])
            else:
                return int("".join(output) + str(int(chars[i]) - 1) + "9"*(L-len(output)-1))

        return int("".join(output))


# Unit Tests
funcs = [Solution().monotoneIncreasingDigits]


class TestMonotoneIncreasingDigits(unittest.TestCase):
    def testMonotoneIncreasingDigits1(self):
        for func in funcs:
            n = 10
            self.assertEqual(func(n=n), 9)

    def testMonotoneIncreasingDigits2(self):
        for func in funcs:
            n = 1234
            self.assertEqual(func(n=n), 1234)

    def testMonotoneIncreasingDigits1(self):
        for func in funcs:
            n = 332
            self.assertEqual(func(n=n), 299)


if __name__ == "__main__":
    unittest.main()
