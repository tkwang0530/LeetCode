"""
204. Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example1:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example2:
    Input: n = 0
    Output: 0
Example3:
    Input: n = 1
    Output: 0

Constraints:
0 <= n <= 5 * 10^6
"""

"""
Note:
1. Remove prime and prime * n in one time: O(n) time | O(n) space
2. Brute-Force: O(n^2) time | O(n) space
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i] == 1:
                primes[i * i : n : i] = [0] * len(primes[i * i : n : i])
        return sum(primes)

    def countPrimes2(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [0] * n
        for i in range(2, n):
            primes[i] = 1 if self.isPrime(i) else 0
        return sum(primes)

    def isPrime(self, num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0 and num != i:
                return False
        return True


# Unit Tests
import unittest


class TestCountPrimes(unittest.TestCase):
    def testCountPrimes1(self):
        func = Solution().countPrimes
        func2 = Solution().countPrimes2
        self.assertEqual(func(n=10), 4)
        self.assertEqual(func2(n=10), 4)

    def testCountPrimes2(self):
        func = Solution().countPrimes
        func2 = Solution().countPrimes2
        self.assertEqual(func(n=0), 0)
        self.assertEqual(func2(n=0), 0)

    def testCountPrimes3(self):
        func = Solution().countPrimes
        func2 = Solution().countPrimes2
        self.assertEqual(func(n=1), 0)
        self.assertEqual(func2(n=1), 0)


if __name__ == "__main__":
    unittest.main()