"""
1101. The Earliest Moment When Everyone Become Friends
There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.

Example1:
Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301
Explanation: 
The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107, and after 2 and 3 become friends, we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211, and after 1 and 5 become friends, we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224, and as 2 and 4 are already friends, nothing happens.
The sixth event occurs at timestamp = 20190301, and after 0 and 3 become friends, we all become friends.

Example2:
Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3
Explanation: At timestamp = 3, all the persons (i.e., 0, 1, 2, and 3) become friends.

Constraints:
2 <= n <= 100
1 <= logs.length <= 10^4
logs[i].length == 3
0 <= timestamp_i <= 10^9
0 <= x_i, y_i <= n - 1
"""

"""
Note:
1. UnionFind + Sort: O(LlogL) time | O(n) space - where L is the length of array logs
"""

import unittest
from typing import List
class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]
        self.counts = [1 for _ in range(n)]
        self.satisfy = False

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False

        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
            self.counts[pv] += self.counts[pu]
        elif self.ranks[pv] < self.ranks[pu]:
            self.parents[pv] = pu
            self.counts[pu] += self.counts[pv]
        else:
            self.parents[pv] = pu
            self.counts[pu] += self.counts[pv]
            self.ranks[pu] += 1
        
        n = len(self.counts)
        self.satisfy = self.satisfy or self.counts[pu] == n or self.counts[pv] == n
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UnionFind(n)
        for timestamp, u, v in logs:
            uf.union(u, v)
            if uf.satisfy:
                return timestamp
        return -1

# Unit Tests
import unittest
funcs = [Solution().earliestAcq]
class TestEarliestAcq(unittest.TestCase):
    def testEarliestAcq1(self):
        for func in funcs:
            logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
            n = 6
            self.assertEqual(func(logs=logs, n=n), 20190301)

    def testEarliestAcq2(self):
        for func in funcs:
            logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
            n = 4
            self.assertEqual(func(logs=logs, n=n), 3)

if __name__ == "__main__":
    unittest.main()
