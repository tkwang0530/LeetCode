"""
526. Beautiful Arrangement
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:
- perm[i] is divisible by i.
- i is divisible by perm[i]

Given an integer n, return the number of the beautiful arrangements that you can construct.

Example1:
Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1

Example2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 15
"""

"""
Note:
1. dfs + memo + bitmask: O(n*2^n) time | O(2^n) space
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        memo = {}
        def dfs(bitmask, number):
            if number == 0:
                return 1
            if bitmask in memo:
                return memo[bitmask]
            result = 0
            for i in range(n):
                used = bitmask & 1 << i
                if not used and ((i+1) % number == 0 or number % (i+1) == 0):
                    result += dfs(bitmask^1<<i, number-1)
            memo[bitmask] = result
            return memo[bitmask]
        return dfs(0, n)
# Unit Tests
import unittest
funcs = [Solution().countArrangement]
class TestCountArrangement(unittest.TestCase):
    def testCountArrangement1(self):
        for func in funcs:
            n = 2
            self.assertEqual(func(n=n), 2)

    def testCountArrangement2(self):
        for func in funcs:
            n = 1
            self.assertEqual(func(n=n), 1)

    def testCountArrangement3(self):
        for func in funcs:
            n = 3
            self.assertEqual(func(n=n), 3)

    def testCountArrangement4(self):
        for func in funcs:
            n = 4
            self.assertEqual(func(n=n), 8)

    def testCountArrangement5(self):
        for func in funcs:
            n = 5
            self.assertEqual(func(n=n), 10)

    def testCountArrangement6(self):
        for func in funcs:
            n = 6
            self.assertEqual(func(n=n), 36)

if __name__ == "__main__":
    unittest.main()
