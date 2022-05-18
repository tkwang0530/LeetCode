"""
403. Frog Jump
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

Example1:
Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.

Example2:
Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.

Constraints:
2 <= stones.length <= 2000
0 <= stones[i] <= 2^31 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.
"""

"""
Note:
1. dfs + memo: O(n^2) time | O(n^2) space - where n is the length of stones
2. dp with HashTable: O(n^2) time | O(n^2) space - where n is the length of stones
kind of like BFS
"""

import collections
from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        stoneIndex = {pos: idx for idx, pos in enumerate(stones)}
        
        memo = {}
        def dfs(i, step):
            if i == len(stones) - 1:
                return True
            
            if (i, step) in memo:
                return memo[(i, step)]
            
            result = False
            for nextStep in [step-1, step, step+1]:
                if nextStep == 0:
                    continue
                if stones[i] + nextStep not in stoneIndex:
                    continue
                
                nextPosition = stones[i] + nextStep
                result = result or dfs(stoneIndex[nextPosition], nextStep)
            memo[(i, step)] = result
            return memo[(i, step)]
        
        return dfs(1, 1)

    def canCross2(self, stones: List[int]) -> bool:
        n = len(stones)
        stoneStepSet = {stone: set() for stone in stones}
        stoneStepSet[0].add(0)
        for i in range(n):
            for k in stoneStepSet[stones[i]]:
                for step in [k-1, k, k+1]:
                    if step > 0 and stones[i] + step in stoneStepSet:
                        stoneStepSet[stones[i] + step].add(step)
        return len(stoneStepSet[stones[-1]]) > 0

# Unit Tests
import unittest
funcs = [Solution().canCross, Solution().canCross2]

class TestCanCross(unittest.TestCase):
    def testCanCross1(self):
        for func in funcs:
            stones = [0,1,3,5,6,8,12,17]
            self.assertEqual(func(stones=stones), True)

    def testCanCross2(self):
        for func in funcs:
            stones = [0,1,2,3,4,8,9,11]
            self.assertEqual(func(stones=stones), False)

if __name__ == "__main__":
    unittest.main()