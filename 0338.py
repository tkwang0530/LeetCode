"""
338. Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
0 <= n <= 10^5
"""

"""
Note:
1. Brute-Force: O(32n) time | O(n) space
2. DP: O(n) time | O(n) space
Index : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
num : 0 1 1 2 1 2 2 3 1 2 2 3 2 3 3 4

dp[index] = dp[index - offset] + 1
"""




import unittest
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            output.append(
                sum([1 if char == "1" else 0 for char in bin(i)[2:]]))
        return output

    def countBits2(self, n: int) -> List[int]:
        output = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            offset = 2*offset if 2*offset == i else offset
            output[i] = output[i - offset] + 1
        return output


# Unit Tests
funcs = [Solution().countBits, Solution().countBits2]


class TestCountBits(unittest.TestCase):
    def testCountBits1(self):
        for func in funcs:
            n = 2
            self.assertEqual(func(n=n), [0, 1, 1])

    def testCountBits2(self):
        for func in funcs:
            n = 5
            self.assertEqual(func(n=n), [0, 1, 1, 2, 1, 2])


if __name__ == "__main__":
    unittest.main()
