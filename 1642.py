"""
1642. Furthest Building You Can Reach
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and remove to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),
- If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
- If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Example1:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example2:
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example3:
Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3

Constraints:
1 <= heights.length <= 10^5
1 <= heights[i] <= 10^6
0 <= bricks <= 10^9
0 <= ladders <= heights.length
"""

"""
Note:
1. dfs + memo (TLE): O(nbL) time | (nbL) space - where n is the length of heights, b is the number of bricks and L is the number of ladders

2. minHeap: O(nlogL) time | O(L) space - where n is the length of heights, L is the number of ladders
"""
import collections, heapq
from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        memo = {}
        def dfs(i, bricks, ladders):
            if bricks < 0 or ladders < 0:
                return 0
            if i == n - 1:
                return n - 1
            if (i, bricks, ladders) in memo:
                return memo[(i, bricks, ladders)]
            else:
                ans = i
                diff = heights[i+1] - heights[i]
                if diff <= 0:
                    ans = dfs(i+1, bricks, ladders)
                else:
                    ans = max(
                        ans,
                        dfs(i+1, bricks-diff, ladders),
                        dfs(i+1, bricks, ladders-1),   
                    )
                memo[(i, bricks, ladders)] = ans
                return memo[(i, bricks, ladders)]
        return dfs(0, bricks, ladders)

    def furthestBuilding2(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        runningLadderBricks = 0
        minHeap = []
        ans = 0
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff < 0:
                ans = i
                continue
            if len(minHeap) < ladders:
                heapq.heappush(minHeap, diff)
            else:
                runningLadderBricks += heapq.heappushpop(minHeap, diff)
            if runningLadderBricks > bricks:
                return i-1
            ans = i
        return ans

# Unit Tests
import unittest
funcs = [Solution().furthestBuilding, Solution().furthestBuilding2]
class TestFurthestBuilding(unittest.TestCase):
    def testFurthestBuilding1(self):
        for func in funcs:
            heights = [4,2,7,6,9,14,12]
            bricks = 5
            ladders = 1
            self.assertEqual(func(heights=heights, bricks=bricks, ladders=ladders), 4)

    def testFurthestBuilding2(self):
        for func in funcs:
            heights = [4,12,2,7,3,18,20,3,19]
            bricks = 10
            ladders = 2
            self.assertEqual(func(heights=heights, bricks=bricks, ladders=ladders), 7)

    def testFurthestBuilding3(self):
        for func in funcs:
            heights = [14,3,19,3]
            bricks = 17
            ladders = 0
            self.assertEqual(func(heights=heights, bricks=bricks, ladders=ladders), 3)

if __name__ == "__main__":
    unittest.main()
