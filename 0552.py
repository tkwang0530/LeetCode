"""
552. Student Attendance Record II
description: https://leetcode.com/problems/student-attendance-record-ii/description/
"""

"""
Note:
1. dfs+memo: O(n*3*2) time | O(n*3*2) space
Memory Limit Exceeded
2. dp: O(n*3*2) time | O(n*3*2) space
"""

import functools
class Solution:
    def checkRecord(self, n: int) -> int:
        M = 10 ** 9 + 7
        # L: how many late i can use consecutively
        # A: how many Absent i can use
        @functools.lru_cache(None)
        def dfs(n, L, A): 
            if n == 0:
                return 1

            total = 0
            # use A is possible
            if A > 0:
                total = (total + dfs(n-1, 2, 0)) % M

            # use L is possible
            if L > 0:
                total = (total + dfs(n-1, L-1, A)) % M

            # use P
            total = (total + dfs(n-1, 2, A)) % M

            return total
        return dfs(n, 2, 1)
    
class Solution2:
    def checkRecord(self, n: int) -> int:
        M = 10 ** 9 + 7

        # dp[i][j][k] represents the number of valid sequences of length i
        # with j consecutive L's and k A's.
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n + 1)]
        
        # Base case: One way to have an empty sequence
        for j in range(3):
            for k in range(2):
                dp[0][j][k] = 1

        for i in range(1, n + 1):
            for j in range(3):
                for k in range(2):
                    # Adding a 'P': resets L count to 0, A count remains the same
                    dp[i][j][k] = dp[i - 1][2][k] % M

                    # Adding a 'L': decrease L count by 1, A count remains the same
                    if j > 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - 1][k]) % M

                    # Adding an 'A': resets L count to 2, decrease A count by 1
                    if k > 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][2][k - 1]) % M

        return dp[n][2][1]

# Unit Tests
import unittest
funcs = [Solution().checkRecord, Solution2().checkRecord]
class TestCheckRecord(unittest.TestCase):
    def testCheckRecord1(self):
        for checkRecord in funcs:
            n = 2
            self.assertEqual(checkRecord(n), 8)

    def testCheckRecord2(self):
        for checkRecord in funcs:
            n = 1
            self.assertEqual(checkRecord(n), 3)

if __name__ == "__main__":
    unittest.main()
