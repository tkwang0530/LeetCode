"""
70. Climbing Stairs
description: https://leetcode.com/problems/climbing-stairs/description/
"""

"""
1. Recursion: O(2^n) time | O(n) space
2. Recursion + caching: O(n) time | O(n) space
3. DP: O(n) time | O(n) space
4. DP (improved): O(n) time | O(1) space
"""




import unittest
class Solution(object):
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs2(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        return self.climbStairs2Helper(n, memo)

    def climbStairs2Helper(self, n: int, memo: dict) -> int:
        if n not in memo:
            memo[n] = self.climbStairs2Helper(
                n-1, memo) + self.climbStairs2Helper(n-2, memo)
        return memo[n]

    def climbStairs3(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]  # last element

    def climbStairs4(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b


# Unit Tests
funcs = [Solution().climbStairs, Solution().climbStairs2,
         Solution().climbStairs3, Solution().climbStairs4]


class TestClimbStairs(unittest.TestCase):
    def testClimbStairs1(self):
        for func in funcs:
            self.assertEqual(func(n=2), 2)

    def testClimbStairs2(self):
        for func in funcs:
            self.assertEqual(func(n=3), 3)

    def testClimbStairs3(self):
        for func in funcs:
            self.assertEqual(func(n=4), 5)


if __name__ == "__main__":
    unittest.main()
