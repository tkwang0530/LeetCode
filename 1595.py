"""
1595. Minimum Cost to Connect Two Groups of Points
description: https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/description/
"""

"""
Note:
1. digital dp: O(size1 * size2 * 2^size2 ) time | O(size1 * 2^size2) space
"""

from typing import List
import functools
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1 = len(cost)
        size2 = len(cost[0])
        
        @functools.lru_cache(None)
        def dfs(mask1, mask2):
            if mask1 == 2**size1-1 and mask2 == 2**size2-1:
                return 0

            minCost = float("inf")
            bin1 = bin(mask1)[2:].zfill(size1)[::-1]
                
            if mask1 < 2**size1 - 1:
                for i in range(size1):
                    if bin1[i] == "1":
                        continue
                    
                    for j in range(size2):
                        minCost = min(minCost, cost[i][j] + dfs((1 << i) | mask1, (1 << j) | mask2))
                    break
            else:
                bin2 = bin(mask2)[2:].zfill(size2)[::-1]
                for j in range(size2):
                    if bin2[j] == "1":
                        continue

                    for i in range(size1):
                        minCost = min(minCost, cost[i][j] + dfs((1 << i) | mask1, (1 << j) | mask2))
                    break

            return minCost
        
        return dfs(0, 0)
# Unit Tests
import unittest
funcs = [Solution().connectTwoGroups]

class TestMaxProductPath(unittest.TestCase):
    def testMaxProductPath1(self):
        for func in funcs:
            cost = [[15, 96], [36, 2]]
            self.assertEqual(func(cost=cost), 17)

    def testMaxProductPath2(self):
        for func in funcs:
            cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
            self.assertEqual(func(cost=cost), 4)

    def testMaxProductPath3(self):
        for func in funcs:
            cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
            self.assertEqual(func(cost=cost), 10)

if __name__ == "__main__":
    unittest.main()