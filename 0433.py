"""
433. Minimum Genetic Mutation
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from  a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.
- For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example1:
Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example2:
Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Example3:
Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3

Constraints:
start.length == 8
end.length == 8
0 <= bank.length <= 10
bank[i].length == 8
start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""

"""
Note:
1. BFS + HashTable: O(3^n * n!) time | O(3^n * n!) space
"""

import collections
from typing import List
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = collections.deque([(start, 0)])
        mutationSet = set(bank)
        options = set(["A", "T", "C", "G"])
        while queue:
            mutation, step = queue.popleft()
            if mutation == end:
                return step
            for i in range(len(mutation)):
                temp = options.copy()
                temp.remove(mutation[i])
                for c in temp:
                    nextMutation = mutation[:i] + c + mutation[i+1:]
                    if nextMutation in mutationSet:
                        mutationSet.remove(nextMutation)
                        queue.append((nextMutation, step+1))
        return -1


# Unit Tests
import unittest
funcs = [Solution().minMutation]
class TestMinMutation(unittest.TestCase):
    def testMinMutation1(self):
        for func in funcs:
            start = "AACCGGTT"
            end = "AACCGGTA"
            bank = ["AACCGGTA"]
            self.assertEqual(func(start=start, end=end, bank=bank), 1)

    def testMinMutation2(self):
        for func in funcs:
            start = "AACCGGTT"
            end = "AAACGGTA"
            bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
            self.assertEqual(func(start=start, end=end, bank=bank), 2)

    def testMinMutation3(self):
        for func in funcs:
            start = "AAAAACCC"
            end = "AACCCCCC"
            bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
            self.assertEqual(func(start=start, end=end, bank=bank), 3)


if __name__ == "__main__":
    unittest.main()
