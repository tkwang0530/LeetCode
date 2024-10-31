"""
2463. Minimum Total Distance Traveled
description: https://leetcode.com/problems/minimum-total-distance-traveled/description
"""

"""
Note:
1. dp (2D): O(R * F * L) time | O(R * F * L) space - where R is the length of array robot and F is the length of factory, and L is the max limit of all the factory 
ref: https://www.youtube.com/watch?v=_wxgR1qMvFE
"""

from typing import List
import unittest
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        # Expand factories into a single list of positions based on limits
        factories = []
        for pos, limit in factory:
            factories.extend([pos] * limit)
        
        m, n = len(robot), len(factories)
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        
        # Base case: no robots left to repair, cost is zero
        for j in range(n + 1):
            dp[0][j] = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Exclude the j-th factory (use previous result in dp[i][j-1])
                dp[i][j] = dp[i][j - 1]
                
                # Include the j-th factory if it reduces cost
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + abs(robot[i - 1] - factories[j - 1]))

        return dp[m][n]

# Unit Tests
funcs = [Solution().minimumTotalDistance]

class TestMinimumTotalDistance(unittest.TestCase):
    def testMinimumTotalDistance1(self):
        for func in funcs:
            robot = [0,4,6]
            factory = [[2,2],[6,2]]
            self.assertEqual(func(robot=robot,factory=factory), 4)

    def testMinimumTotalDistance2(self):
        for func in funcs:
            robot = [1,-1]
            factory = [[-2,1],[2,1]]
            self.assertEqual(func(robot=robot,factory=factory), 2)

if __name__ == "__main__":
    unittest.main()
