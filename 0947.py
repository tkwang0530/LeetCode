"""
947. Most Stones Removed with Same Row or Column
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [x_i, y_i] represents the location of the ith stone, return the largest possible number of stones that can be removed.

Example1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example3:
Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

Constraints:
1 <= stones.length <= 1000
0 <= x_i, y_i <= 10^4
No two stones are at the same coordinate point.
"""

"""
Note:
1. Union Find: O(n) time | O(n) space
(1) Separate one stone into two parts: x coordinate unit and y coordinate unit, for example stone in (3,5) => 3y and 5x
(2) add these two parts into the stoneLocationSet
(3) merge these two parts
"""


from typing import List
import unittest

class UnionFindSet:
    def __init__(self, n):
        self._parents = {} # <string, string>
        self._ranks = {} # <string, int>
        self.exists = 0

    def add(self, location):
        if location not in self._parents:
            self._parents[location] = location
            self._ranks[location] = 1
            self.exists += 1

    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u
    
    def union(self, u, v) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:
            self._parents[pv] = pu
            self._ranks[pu] += 1
        self.exists -= 1
        return True
    

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stoneLocationSet = UnionFindSet(len(stones))
        for stone in stones:
            x = str(stone[1]) + "x"
            y = str(stone[0]) + "y"
            stoneLocationSet.add(x)
            stoneLocationSet.add(y)

            stoneLocationSet.union(x, y)
        return len(stones) - stoneLocationSet.exists


# Unit Tests
funcs = [Solution().removeStones]

class TestRemoveStones(unittest.TestCase):
    def testRemoveStones1(self):
        for func in funcs:
            stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
            self.assertEqual(func(stones=stones), 5)

    def testRemoveStones2(self):
        for func in funcs:
            stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
            self.assertEqual(func(stones=stones), 3)

    def testRemoveStones3(self):
        for func in funcs:
            stones = [[0,0]]
            self.assertEqual(func(stones=stones), 0)


if __name__ == "__main__":
    unittest.main()
