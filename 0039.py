"""
39. Combination Sum
description: https://leetcode.com/problems/combination-sum/description/
"""

"""
Note:
1. DFS: O(2^k) time | O(target) space
where k is the sum of (target / candidate)
"""


import unittest
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        output = []
        current = []
        def backtrack(i, target):
            if i == n or target <= 0:
                if target == 0:
                    output.append(current.copy())
                return
            
            value = candidates[i]
            
            # not take
            backtrack(i+1, target)

            # take
            current.append(value)
            backtrack(i, target-value)
            current.pop()
        backtrack(0, target)
        return output

# Unit Tests
funcs = [Solution().combinationSum]


class TestCombinationSum(unittest.TestCase):
    def testCombinationSum1(self):
        for func in funcs:
            candidates = [2,3,6,7]
            target = 7
            self.assertEqual(
                sorted(func(candidates=candidates, target=target)),
                sorted([[2,2,3],[7]]),
            )

    def testCombinationSum2(self):
        for func in funcs:
            candidates = [2,3,5]
            target = 8
            self.assertEqual(
                sorted(func(candidates=candidates, target=target)),
                sorted([[2,2,2,2],[2,3,3],[3,5]]),
            )

    def testCombinationSum3(self):
        for func in funcs:
            candidates = [2]
            target = 1
            self.assertEqual(
                sorted(func(candidates=candidates, target=target)),
                sorted([]),
            )
    
    def testCombinationSum4(self):
        for func in funcs:
            candidates = [1]
            target = 1
            self.assertEqual(
                sorted(func(candidates=candidates, target=target)),
                sorted([[1]]),
            )

    def testCombinationSum5(self):
        for func in funcs:
            candidates = [1]
            target = 2
            self.assertEqual(
                sorted(func(candidates=candidates, target=target)),
                sorted([[1, 1]]),
            )
    


if __name__ == "__main__":
    unittest.main()
