"""
216. Combination Sum III
description: https://leetcode.com/problems/combination-sum-iii/description/
"""

"""
Note:
1. backtracking: O(k * C(n,k)) time | O(k) space
"""

import unittest
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        current = []
        def backtrack(k, n, minNum):
            if k == 0:
                if n == 0:
                    output.append(current.copy())
                return

            if n <= 0:
                return

            for num in range(minNum, 9+1):
                current.append(num)
                backtrack(k-1, n-num, num+1)
                current.pop()
        
        backtrack(k, n, 1)
        return output

# Unit Tests
funcs = [Solution().combinationSum3]


class TestCombinationSum(unittest.TestCase):
    def testCombinationSum1(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(k=3, n=7)),
                sorted([[1,2,4]]),
            )

    def testCombinationSum2(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(k=3, n=9)),
                sorted([[1,2,6],[1,3,5],[2,3,4]]),
            )

    def testCombinationSum3(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(k=4, n=1)),
                sorted([]),
            )

    def testCombinationSum4(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(k=3, n=2)),
                sorted([]),
            )

    def testCombinationSum5(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(k=9, n=45)),
                sorted([[1,2,3,4,5,6,7,8,9]]),
            )


if __name__ == "__main__":
    unittest.main()
