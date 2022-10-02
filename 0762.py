"""
762. Prime Number of Set Bits in Binary Representation
Given two integers left and right ,return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.
- For example, 21 written in binary is 10101, which has 3 set bits.

Example1:
Input: left = 6, right = 10
Output: 4
Explanation:
6  -> 110 (2 set bits, 2 is prime)
7  -> 111 (3 set bits, 3 is prime)
8  -> 1000 (1 set bit, 1 is not prime)
9  -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.

Example2:
Input: left = 10, right = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
5 numbers have a prime number of set bits.

Constraints:
1 <= left <= right <= 10^6
0 <= right - left <= 10^4
"""

"""
Note:
1. Brute-Force: O(right-left+1) time | O(1) space
"""




import unittest
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        output = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        for num in range(left, right+1):
            count = bin(num).count("1")
            if count in primes:
                output += 1
        return output


# Unit Tests
funcs = [Solution().countPrimeSetBits]


class TestCountPrimeSetBits(unittest.TestCase):
    def testCountPrimeSetBits1(self):
        for func in funcs:
            left = 6
            right = 10
            self.assertEqual(func(left=left, right=right), 4)

    def testCountPrimeSetBits2(self):
        for func in funcs:
            left = 10
            right = 15
            self.assertEqual(func(left=left, right=right), 5)


if __name__ == "__main__":
    unittest.main()
