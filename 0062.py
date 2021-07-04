"""
62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example1:
Input: m = 3, n = 7
Output: 28

Example2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example3:
Input: m = 7, n = 3
Output: 28

Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10^9
"""

"""
1. Recursion: O(2^(m+n)) time | O(m + n ) space
2. Recursion + caching: O(mn) time | O(mn) space
3. DP: O(mn) time | O(mn space)
4. DP (improved): O(mn) time | O(min(m, n))
"""




import unittest
class Solution(object):
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:  # base case
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    def uniquePaths2(self, m: int, n: int) -> int:
        memo = {}
        return self.uniquePaths2Helper(m, n, memo)

    def uniquePaths2Helper(self, m, n, memo) -> int:
        if m == 1 or n == 1:  # base case
            return 1
        if (m, n) not in memo:
            memo[(m, n)] = self.uniquePaths2Helper(m - 1, n, memo) + \
                self.uniquePaths2Helper(m, n - 1, memo)
        return memo[(m, n)]

    def uniquePaths3(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m):  # prefill
            dp.append([1] * n)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths4(self, m: int, n: int) -> int:
        if n > m:
            n, m = m, n
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]


# Unit Tests
funcs = [Solution().uniquePaths, Solution().uniquePaths2,
         Solution().uniquePaths3, Solution().uniquePaths4]


class TestUniquePaths(unittest.TestCase):
    def testUniquePaths1(self):
        for func in funcs:
            self.assertEqual(func(m=3, n=7), 28)

    def testUniquePaths2(self):
        for func in funcs:
            self.assertEqual(func(m=3, n=2), 3)

    def testUniquePaths3(self):
        for func in funcs:
            self.assertEqual(func(m=7, n=3), 28)

    def testUniquePaths4(self):
        for func in funcs:
            self.assertEqual(func(m=3, n=3), 6)


if __name__ == "__main__":
    unittest.main()
