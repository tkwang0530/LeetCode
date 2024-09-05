"""
2028. Find Missing Observations
description: https://leetcode.com/problems/find-missing-observations/description/
"""

"""
Note:
1. Greedy: O(n+m) time | O(n) space
"""

import unittest
from typing import List
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        mSum = sum(rolls)
        nSum = mean * (m+n) - mSum
        base = nSum // n
        
        if nSum > 6*n or nSum < n:
            return []

        nSum %= n
        nRolls = [base] * n
        i = 0
        while nSum > 0:
            cost = min(nSum, 6-nRolls[i])
            nRolls[i] += cost
            nSum -= cost
            i += 1
        return nRolls

# Unit Tests
import unittest
funcs = [Solution().missingRolls]
class TestMissingRolls(unittest.TestCase):
    def testMissingRolls1(self):
        for func in funcs:
            rolls = [3,2,4,3]
            mean = 4
            n = 2
            self.assertEqual(func(rolls=rolls, mean=mean, n=n), [6,6])

    def testMissingRolls2(self):
        for func in funcs:
            rolls = [1,5,6]
            mean = 3
            n = 4
            self.assertEqual(func(rolls=rolls, mean=mean, n=n), [3,2,2,2])

    def testMissingRolls3(self):
        for func in funcs:
            rolls = [1,2,3,4]
            mean = 6
            n = 4
            self.assertEqual(func(rolls=rolls, mean=mean, n=n), [])

if __name__ == "__main__":
    unittest.main()
