"""
1202. Smallest String With Swaps
You are given a string s, and an array of pairs of indices in the string pairs where pairs = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number times.

Return the lexicographically smallest string that s can be changed to after using swaps.

Example1:
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example2:
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example3:
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

Constraints:
1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
"""

"""
Note:
1. UnionFind + Counting Sort: O(n+m) time | O(n) space - where n is the length of string s and m is the length of array pairs
"""
from typing import List
import collections
class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

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
        elif self.ranks[pv] < self.ranks[pu]:
            self.parents[pv] = pu
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1
        return True

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        unionFind = UnionFind(n)
        for u, v in pairs:
            unionFind.union(u, v)

        parentGroups = collections.defaultdict(list)
        for i in range(n):
            parentGroups[unionFind.find(i)].append(i)

        def countingSort(arr: List[str]) -> List[str]:
            counter = [0] * 26
            sortedArr = []
            for char in arr:
                counter[ord(char) - ord('a')] += 1
            for i in range(26):
                char = chr(i + ord('a'))
                count = counter[i]
                sortedArr.extend([char] * count)
            return sortedArr

        resChars = [""] * n
        for indice in parentGroups.values():
            chars = [s[i] for i in indice]
            sortedArr = countingSort(chars)
            for i,char in zip(indice, sortedArr):
                resChars[i] = char

        return "".join(resChars)

# Unit Tests
import unittest
funcs = [Solution().smallestStringWithSwaps]
class TestSmallestStringWithSwaps(unittest.TestCase):
    def testSmallestStringWithSwaps1(self):
        for func in funcs:
            s = "dcab"
            pairs = [[0,3],[1,2]]
            self.assertEqual(func(s=s, pairs=pairs), "bacd")

    def testSmallestStringWithSwaps2(self):
        for func in funcs:
            s = "dcab"
            pairs = [[0,3],[1,2],[0,2]]
            self.assertEqual(func(s=s, pairs=pairs), "abcd")

    def testSmallestStringWithSwaps3(self):
        for func in funcs:
            s = "cba"
            pairs = [[0,1],[1,2]]
            self.assertEqual(func(s=s, pairs=pairs), "abc")

    def testSmallestStringWithSwaps4(self):
        for func in funcs:
            s = "tklkxyizmlqf"
            pairs = [[2,10],[3,5],[8,11],[1,2],[10,6],[4,1],[1,10],[5,8],[8,3],[10,4],[7,3],[10,11]]
            self.assertEqual(func(s=s, pairs=pairs), "tfikklmqxlyz")

if __name__ == "__main__":
    unittest.main()
