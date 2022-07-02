"""
276. Paint Fence
You are painting a fence of n posts with k different colors. You must paint the posts following these rules:
- Every post must be painted exactly one color.
- There cannot be three or more consecutive posts with the same color.

Given the two integers n and k, return the number of ways you can paint the fence.

Example1:
Input: n = 3, k = 2
Output: 6
Explanation: All the possibilities are shown.
Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.

Example2:
Input: n = 1, k = 1
Output: 1

Example3:
Input: n = 7, k = 2
Output: 42

Constraints:
1 <= n <= 50
1 <= k <= 10^5
The testcases are generated such that the answer is in the range [0, 2^31 - 1] for the given n and k.
"""

"""
Note:
1. DP: O(n) time | O(1) space
If you are painting the i-th post, you have two options:
(1) make it different color as i-1 th post
(2) make it same color as i-1 th post (if you are allowed!)
num_ways[i] = num_ways_diff[i] + num_ways_same[i]
num_ways_diff[i] = num_ways[i-1] * (k-1)
num_ways_same[i] = num_ways_diff[i-1] * 1
=> num_ways[i] = num_ways[i-1] * (k-1) + num_ways[i-2] * (k-1) = [num_ways[i-1] + num_ways[i-2]] * (k-1)
"""

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0: return 0
        if n == 1: return k
        if n == 2: return k*k
        dp0, dp1 = k, k*k
        for _ in range(n-2):
            dp0, dp1 = dp1, (dp0+dp1)*(k-1)
        return dp1

# Unit Tests
import unittest
funcs = [Solution().numWays]
class TestNumWays(unittest.TestCase):
    def testNumWays1(self):
        for func in funcs:
            n = 3
            k = 2
            self.assertEqual(func(n=n, k=k), 6)

    def testNumWays2(self):
        for func in funcs:
            n = 1
            k = 1
            self.assertEqual(func(n=n, k=k), 1)

    def testNumWays3(self):
        for func in funcs:
            n = 7
            k = 2
            self.assertEqual(func(n=n, k=k), 42)

    def testNumWays4(self):
        for func in funcs:
            n = 3
            k = 3
            self.assertEqual(func(n=n, k=k), 24)


if __name__ == "__main__":
    unittest.main()
