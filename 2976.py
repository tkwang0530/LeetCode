"""
2976. Minimum Cost to Convert String I
description: https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/
"""

"""
Note:
1. Floyd Warshall: O(26^3+n+c) time | O(26^2) space - where n is the length of string source and c is the length of array cost
"""

from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[float("inf")] * 26 for _ in range(26)]
        costLen = len(cost)
        for i in range(costLen):
            uChar, vChar, d = original[i], changed[i], cost[i]
            u, v = ord(uChar)-ord('a'), ord(vChar)-ord('a')
            dist[u][v] = min(dist[u][v], d)

        for k in range(26):
            for u in range(26):
                for v in range(26):
                    dist[u][v] = min(dist[u][v], dist[u][k]+dist[k][v])

        minCost = 0
        for i in range(len(source)):
            uChar, vChar = source[i], target[i]
            u, v = ord(uChar)-ord('a'), ord(vChar)-ord('a')
            if u != v:
                if dist[u][v] == float('inf'):
                    return -1
                minCost += dist[u][v]

        return minCost

# Unit Tests
import unittest
funcs = [Solution().minimumCost]

class TestMinimumCost(unittest.TestCase):
    def testMinimumCost1(self):
        for func in funcs:
            source = "abcd"
            target = "acbe"
            original = ["a","b","c","c","e","d"]
            changed = ["b","c","b","e","b","e"]
            cost = [2,5,5,1,2,20]
            self.assertEqual(func(source=source, target=target, original=original, changed=changed, cost=cost), 28)

    def testMinimumCost2(self):
        for func in funcs:
            source = "aaaa"
            target = "bbbb"
            original = ["a","c"]
            changed = ["c","b"]
            cost = [1,2]
            self.assertEqual(func(source=source, target=target, original=original, changed=changed, cost=cost), 12)

    def testMinimumCost3(self):
        for func in funcs:
            source = "abcd"
            target = "abce"
            original = ["a"]
            changed = ["e"]
            cost = [10000]
            self.assertEqual(func(source=source, target=target, original=original, changed=changed, cost=cost), -1)

if __name__ == "__main__":
    unittest.main()
