"""
1722. Minimize Hamming Distance After Swap Operations
You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [a_i, b_i] indicates that you are allowed to swap the elements at index a_i and index b_i (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.

The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).

Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.

Example1:
Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
Output: 1
Explanation: source can be transformed the following way:
- Swap indices 0 and 1: source = [2,1,3,4]
- Swap indices 2 and 3: source = [2,1,4,3]
The Hamming distance of source and target is 1 as they differ in 1 position: index 3.

Example2:
Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
Output: 2
Explanation: There are no allowed swaps.
The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.

Example3:
Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
Output: 0

Constraints:
n == source.length == target.length
1 <= n <= 10^5
1 <= source[i], target[i] <= 10^5
0 <= allowedSwaps.length <= 10^5
allowedSwaps[i].length == 2
0 <= a_i, b_i <= n - 1
a_i != b_i
"""

"""
Note:
1. UnionFind + HashTable: O(N+E) time | O(N+E) space - where N is the length of array source and E is the length of array allowedSwaps
"""

import collections
from typing import List
class UnionFind:
    def __init__(self, n) -> None:
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

    def find(self, u) -> int:
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False

        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pv] < self.ranks[pu]:
            self.parents[pv] = pu
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1
        return True

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)

        for idx1, idx2 in allowedSwaps:
            uf.union(idx1, idx2)
        
        indexGroups = [collections.Counter() for _ in range(n)]
        for i, num in enumerate(source):
            indexGroups[uf.find(i)][num] += 1

        result = 0
        for i, num in enumerate(target):
            indexGroups[uf.find(i)][num] -= 1
            if indexGroups[uf.find(i)][num] < 0:
                result += 1

        return result



# Unit Tests
import unittest
funcs = [Solution().minimumHammingDistance]
class TestMinimumHammingDistance(unittest.TestCase):
    def testMinimumHammingDistance1(self):
        for func in funcs:
            source = [1,2,3,4]
            target = [2,1,4,5]
            allowedSwaps = [[0,1],[2,3]]
            self.assertEqual(func(source=source, target=target, allowedSwaps=allowedSwaps), 1)

    def testMinimumHammingDistance2(self):
        for func in funcs:
            source = [1,2,3,4]
            target = [1,3,2,4]
            allowedSwaps = []
            self.assertEqual(func(source=source, target=target, allowedSwaps=allowedSwaps), 2)

    def testMinimumHammingDistance3(self):
        for func in funcs:
            source = [5,1,2,4,3]
            target = [1,5,4,2,3]
            allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
            self.assertEqual(func(source=source, target=target, allowedSwaps=allowedSwaps), 0)


if __name__ == "__main__":
    unittest.main()
