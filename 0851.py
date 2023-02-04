"""
851. Loud and Rich
There is a group of n people labeled from 0 to n-1 where each person has a different amount of money and a different level of quietness.

You are given an array richer where richer[i] = [a_i, b_i] indicates that a_i has more money than b_i and an integer array quiet where quiet[i] is the quietness of the i-th person. All the given data in richer are logically correct (i.e., the data will not lead you to a situation where x is richer than y and y is richer than x at the same time).

Return an integer array answer where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]) among all people who definitely have equal to or more money than the person x.

Example1:
Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation: 
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but it is not clear if they have more money than person 0.
answer[7] = 7.
Among all people that definitely have equal to or more money than person 7 (which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x]) is person 7.
The other answers can be filled out with similar reasoning.

Example2:
Input: richer = [], quiet = [0]
Output: [0]

Constraints:
n == quiet.length
1 <= n <= 500
0 <= quiet[i] < n
All the values of quiet are unique.
0 <= richer.length <= n * (n-1) / 2
0 <= a_i, b_i < n
a_i != b_i
All the pairs of richer are unique.
The observations in richer are all logically consistent.
"""

"""
Note:
1. Layer order Traversal: O(r+q) time | O(r+q) space - where r is the length of array richer and q is the length of array quiet
"""




import unittest
import collections
from typing import List
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        answer = [i for i in range(n)]
        minParent = [quiet[i] for i in range(n)]
        degree = [0] * n
        graph = collections.defaultdict(list)
        for parent, child in richer:
            graph[parent].append(child)
            degree[child] += 1

        currentSet = set()
        for idx in range(n):
            if degree[idx] == 0:
                currentSet.add(idx)

        while currentSet:
            nextSet = set()
            for parent in currentSet:
                for child in graph[parent]:
                    if minParent[parent] < minParent[child]:
                        minParent[child] = minParent[parent]
                        answer[child] = answer[parent]
                    degree[child] -= 1
                    if degree[child] == 0:
                        nextSet.add(child)
            currentSet = nextSet
        return answer


# Unit Tests
funcs = [Solution().loudAndRich]


class TestLoudAndRich(unittest.TestCase):
    def testLoudAndRich1(self):
        for func in funcs:
            richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
            quiet = [3, 2, 5, 4, 6, 1, 7, 0]
            self.assertEqual(func(richer=richer, quiet=quiet),
                             [5, 5, 2, 5, 4, 5, 6, 7])

    def testLoudAndRich2(self):
        for func in funcs:
            richer = []
            quiet = [0]
            self.assertEqual(func(richer=richer, quiet=quiet), [0])


if __name__ == "__main__":
    unittest.main()
