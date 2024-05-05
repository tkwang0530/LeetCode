"""
40. Combination Sum II
description: https://leetcode.com/problems/combination-sum-ii/description/
"""

"""
Note:
1. DFS: O(2^n*target) time | O(target) space - where n is the length of candidates
(1) candidates may only be used once i + 1
(2) not contain duplicate combinations: sort + A[i] == A[i-1] continue
"""


import unittest
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        output = []
        current = []
        def backtrack(i, runningSum):
            if runningSum == target:
                output.append(current.copy())
                return

            if runningSum > target or i == n:
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
            
                # include
                current.append(candidates[j])
                backtrack(j+1, runningSum+candidates[j])
                current.pop()
            
        backtrack(0, 0)
        return output

# Unit Tests
funcs = [Solution().combinationSum2]


class TestCombinationSum(unittest.TestCase):
    def testCombinationSum1(self):
        for func in funcs:
            candidates = [10,1,2,7,6,1,5]
            target = 8
            self.assertEqual(
                sorted(func(candidates=candidates, target=target)),
                sorted([[1,1,6],[1,2,5],[1,7],[2,6]]),
            )

    def testCombinationSum2(self):
        for func in funcs:
            candidates = [2,5,2,1,2]
            target = 5
            self.assertEqual(
                sorted(func(candidates=candidates, target=target)),
                sorted([[1,2,2],[5]]),
            )


if __name__ == "__main__":
    unittest.main()
