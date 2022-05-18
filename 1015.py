"""
1015. Smallest Integer Divisible by K
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

Example1:
Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.

Example2:
Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.

Example3:
Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.

Constraints:
1 <= k <= 10^5
"""

"""
Note:
1. HashTable: O(k) time | O(k) space
record remainders
"""

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        length = 1
        currNum = 1
        remainders = set()
        while currNum > 0:
            if currNum % k in remainders:
                return -1
            remainders.add(currNum % k)
            while currNum < k:
                currNum *= 10
                currNum += 1
                length += 1
            currNum = currNum % k
        return length

# Unit Tests
import unittest
funcs = [Solution().smallestRepunitDivByK]

class TestsmallestRepunitDivByK(unittest.TestCase):
    def testsmallestRepunitDivByK1(self):
        for func in funcs:
            k = 1
            self.assertEqual(func(k=k), 1)

    def testsmallestRepunitDivByK2(self):
        for func in funcs:
            k = 2
            self.assertEqual(func(k=k), -1)

    def testsmallestRepunitDivByK3(self):
        for func in funcs:
            k = 3
            self.assertEqual(func(k=k), 3)

if __name__ == "__main__":
    unittest.main()