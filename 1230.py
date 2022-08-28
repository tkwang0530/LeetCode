"""
1230. Toss Strange Coins
You have some coins. The i-th coin has a probability prob[i] of facing heads when tossed.

Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.

Example1:
Input: prob = [0.4], target = 1
Output: 0.40000

Example2:
Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
Output: 0.03125

Constraints:
1 <= prob.length <= 1000
0 <= prob[i] <= 1
0 <= target <= prob.length
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
"""

"""
Note:
1. DFS+memo: O(n * target) time | O(n * target) space - where n is the length of array prob
"""

from typing import List
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        memo = {}
        def dfs(i, target):
            if target < 0:
                return 0
            if i >= len(prob):
                return target == 0
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            memo[(i, target)] = prob[i] * dfs(i+1, target-1) + (1-prob[i]) * dfs(i+1, target)
            return memo[(i, target)]
        return dfs(0, target)

# Unit Tests
import unittest
funcs = [Solution().probabilityOfHeads]
class TestProbabilityOfHeads(unittest.TestCase):
    def testProbabilityOfHeads1(self):
        for func in funcs:
            prob = [0.4]
            target = 1
            self.assertEqual(func(prob=prob, target=target), 0.4)

    def testProbabilityOfHeads2(self):
        for func in funcs:
            prob = [0.5,0.5,0.5,0.5,0.5]
            target = 0
            self.assertEqual(func(prob=prob, target=target), 0.03125)

if __name__ == "__main__":
    unittest.main()
