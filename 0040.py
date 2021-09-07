"""
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a taget number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
]

Example2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
    [1,2,2],
    [5]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

"""
Note:
1. DFS: O(2^n) time | O(target) space - where n is the length of candidates
(1) candidates may only be used once i + 1
(2) not contain duplicate combinations: sort + A[i] == A[i-1] continue
"""


import unittest
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or len(candidates) == 0:
            return []
        candidates.sort()
        result = []
        self.dfs(candidates, target, [], result, 0)
        return result

    def dfs(self, candidates: List[int], target: int, current: List[int], result: List[List[int]],index: int) -> None:
        if target < 0:
            return
        if target == 0:
            result.append(current[:])
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            current.append(candidates[i])
            self.dfs(candidates, target - candidates[i], current, result, i + 1)
            current.pop()

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
