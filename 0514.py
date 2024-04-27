"""
514. Freedom Trail
description: https://leetcode.com/problems/freedom-trail/description/
"""

"""
Note:
1. dfs+memo: O(r^2*k) time | O(r*k) space - where r is the length of ring and k is the length of key
ref: https://www.youtube.com/watch?v=NOgnlTXidSs

2. dp: O(r^2*k) time | O(r) space - where r is the length of ring and k is the length of key
"""

import unittest, functools
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @functools.lru_cache(None)
        def dfs(r, k):
            if k == len(key):
                return 0
            
            minSteps = float("inf")
            for i, char in enumerate(ring):
                if char == key[k]:
                    dist = min(
                        abs(r-i), # between
                        len(ring)-abs(r-i) # round
                    )
                    minSteps = min(minSteps, dist + 1 + dfs(i, k+1))
            return minSteps

        return dfs(0, 0)

class Solution2:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [0] * len(ring)
        for k in reversed(range(len(key))):
            nextDP = [float("inf")] * len(ring)
            for r in range(len(ring)):
                for i, char in enumerate(ring):
                    if char == key[k]:
                        dist = min(
                            abs(r-i), # between
                            len(ring)-abs(r-i) # round
                        )
                        nextDP[r] = min(nextDP[r], dist + 1 + dp[i])
            dp = nextDP
        return dp[0]

# Unit Tests
import unittest
funcs = [Solution().findRotateSteps, Solution2().findRotateSteps]
class TestFindRotateSteps(unittest.TestCase):
    def testFindRotateSteps1(self):
        for func in funcs:
            ring = "godding"
            key = "gd"
            self.assertEqual(func(ring=ring, key=key), 4)

    def testFindRotateSteps2(self):
        for func in funcs:
            ring = "godding"
            key = "godding"
            self.assertEqual(func(ring=ring, key=key), 13)

if __name__ == "__main__":
    unittest.main()
