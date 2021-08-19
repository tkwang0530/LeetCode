"""
547. Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces

Example1:
1 -  2

3
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example2:
1     2

3
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
1 <= n <= 200
n == isConnected.length
m == isConnected[i].length
isConnected[i][j] == 1 or 0
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

"""
Note:
1. Recursive DFS: O(n^2) time | O(n) space
2. Union-Find (using manual UnionFindSet): O(n^n) time | O(n) space
"""

from typing import List
import unittest


class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n+1)]
        self._ranks = [1 for _ in range(n+1)]

    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def union(self, u, v):
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
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not any(isConnected):
            return 0
        visited = [0] * len(isConnected)
        numOfCircle = 0
        for city in range(len(isConnected)):
            if visited[city]:
                continue
            visited[city] = 1
            self.dfs(isConnected, city, visited)
            numOfCircle += 1
        return numOfCircle
    
    def dfs(self, isConnected, city, visited) -> None:
        for otherCity in range(len(isConnected)):
            if isConnected[city][otherCity] and not visited[otherCity]:
                visited[otherCity] = 1
                self.dfs(isConnected, otherCity, visited)

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        if not any(isConnected):
            return 0
        unionFindSet = UnionFindSet(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j]:
                    unionFindSet.union(i, j)
        provinces = set()
        for i in range(len(isConnected)):
            provinces.add(unionFindSet.find(i))
        return len(provinces)

# Unit Tests
funcs = [Solution().findCircleNum, Solution().findCircleNum2]


class TestFindCircleNum(unittest.TestCase):
    def testFindCircleNum1(self):
        for func in funcs:
            isConnected = [[1,1,0],[1,1,0],[0,0,1]]
            self.assertEqual(func(isConnected=isConnected), 2)

    def testFindCircleNum2(self):
        for func in funcs:
            isConnected = [[1,0,0],[0,1,0],[0,0,1]]
            self.assertEqual(func(isConnected=isConnected), 3)

if __name__ == "__main__":
    unittest.main()
