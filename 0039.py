"""
39. Given an array of distinct integers "candidates" and a target integer "target", return a list of all unique combinations of candidates where the chosen numbers sum to "target". You may return the combinations in any order

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example3:
Input: candidates = [2], target = 1
Output: []

Example4:
Input: candidates = [1], target = 1
Output: [[1]]

Example5:
Input: candidates = [1], target = 2
Output: [[1,1]]

Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
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
        if not candidates:
            return []
        result = []
        self.dfs(candidates, target, [], result, 0)
        return result

    def dfs(self, candidates: List[int], target: int, current: List[int], result: List[List[int]], index: int):
        if target < 0:
            return
        if target == 0:
            result.append(current[:])
            return
        
        for i in range(index, len(candidates)):
            current.append(candidates[i])
            # not index+1 because we can reuse same elements
            self.dfs(candidates, target - candidates[i], current, result, i)
            current.pop()

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
