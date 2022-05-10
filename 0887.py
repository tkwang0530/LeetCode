"""
887. Super Egg Drop
You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where i <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.

Example1:
Input: k = 1, n = 2
Output: 2
Explanation: 
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.

Example2:
Input: k = 2, n = 6
Output: 3

Example3:
Input: k = 3, n = 14
Output: 4

Constraints:
1 <= k <= 100
1 <= n <= 10^4
"""

"""
Note:
1. DFS + memo: O(n^2*k) time | O(nk) space
2. DFS + Binary Search + memo: O(nlogn*k) time | O(nk) space
3. DP (lee215): O(nk+klogn) time | O(nk) space

dp[M][K] means that given K eggs and M moves, what is the maximum number of floor that we can check
dp[m][k] = dp[m-1][k-1] + dp[m-1][k] + 1,
which means we take 1 move to a floor,
if egg breaks, then we can check dp[m-1][k-1] floors.
if egg doesn't break, then we can check dp[m-1][k] floors.

dp[m][k] is the number of combinations and it increases exponentially to N

4. DP-1D (lee215): O(k+klogn) time | O(k) space
"""

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}
        def dfs(n, k):
            if n <= 1:
                return n
            if k == 1:
                return n

            if (n, k) in memo:
                return memo[(n, k)]

            minTries = float("inf")
            for f in range(n // 2 + 1, 0, -1):
                minTries = min(
                    minTries,
                    max(dfs(f-1, k-1), dfs(n-f, k))
                )
            
            # 1 tries + otherMinTries
            memo[(n, k)] = minTries + 1
            return memo[(n, k)]
        return dfs(n, k)

    def superEggDrop2(self, k: int, n: int) -> int:
        memo = {}
        def dfs(n, k):
            if n <= 1:
                return n
            if k == 1:
                return n

            if (n, k) in memo:
                return memo[(n, k)]

            minTries = float("inf")

            left, right = 1, n // 2 + 2
            while left < right:
                mid = left + (right - left) // 2
                breaks = dfs(mid-1, k-1)
                notBreaks = dfs(n-mid, k)
                minTries = min(
                    minTries,
                    max(breaks, notBreaks)
                )
                if breaks < notBreaks:
                    left = mid + 1
                else:
                    right = mid
            
            # 1 tries + otherMinTries
            memo[(n, k)] = minTries + 1
            return memo[(n, k)]
        return dfs(n, k)

    def superEggDrop3(self, k: int, n: int) -> int:
        dp = [[0] * (k+1) for _ in range(n+1)]
        for m in range(1, n+1):
            for tempK in range(1, k+1):
                dp[m][tempK] = dp[m-1][tempK-1] + dp[m-1][tempK] + 1
            if dp[m][tempK] >= n:
                return m

    def superEggDrop4(self, k: int, n: int) -> int:
        dp0 = [0] * (k+1)
        for m in range(1, n+1):
            dp1 = [0] * (k+1)
            for tempK in range(1, k+1):
                dp1[tempK] = dp0[tempK-1] + dp0[tempK] + 1
            if dp1[tempK] >= n:
                return m
            dp0 = dp1

# Unit Tests
import unittest
funcs = [Solution().superEggDrop, Solution().superEggDrop2, Solution().superEggDrop3, Solution().superEggDrop4]

class TestSuperEggDrop(unittest.TestCase):
    def testSuperEggDrop1(self):
        for func in funcs:
            k = 1
            n = 2
            self.assertEqual(func(k=k, n=n), 2)

    def testSuperEggDrop2(self):
        for func in funcs:
            k = 2
            n = 6
            self.assertEqual(func(k=k, n=n), 3)

    def testSuperEggDrop3(self):
        for func in funcs:
            k = 3
            n = 14
            self.assertEqual(func(k=k, n=n), 4)

if __name__ == "__main__":
    unittest.main()